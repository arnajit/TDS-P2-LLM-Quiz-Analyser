🚀 TDS Project – Automated Quiz Solving API (FastAPI + LangGraph + Gemini + Playwright)

This repository implements a fully automated Task-Driven Data Science (TDS) quiz-solving agent.
It is designed to handle multi-step quiz URLs, extract data from web pages, solve analytical tasks, and respond correctly within strict time limits using a headless browser and LLM-powered reasoning.

This project powers a backend FastAPI endpoint used for evaluation on TDS servers.

📌 Features
✅ FastAPI endpoint for receiving quiz tasks

Validates email, secret, and quiz URL

Responds with proper status codes: 200, 400, 403

Runs the agent asynchronously using background tasks

Uses /solve as the main entrypoint

✅ Autonomous Agent (LangGraph + Gemini 2.5 Flash)

The agent can:

Load quiz pages (including JS-rendered pages via Playwright)

Extract instructions and submission endpoints

Download and parse files (CSV/PDF/Images/Audio)

Perform OCR using Gemini Vision

Transcribe audio using SpeechRecognition

Execute Python code safely inside sandbox

Submit answers using the exact endpoint defined in the quiz

Handle:

Retries

Timeouts

Multi-step quiz chains

Base64 encodings

Audio transcription

Malformed JSON tool calls

Server-provided “next URL” sequences

✅ Advanced Tools Included
Tool	Purpose
get_rendered_html	JS rendering using Playwright Chromium
download_file	Save remote files into LLMFiles/
encode_image_to_base64	Safe Base64 encoding via shared store
ocr_image_tool	Gemini Vision OCR
transcribe_audio	MP3 → WAV → speech-to-text
run_code	Controlled Python execution
add_dependencies	Install missing packages via uv
post_request	Safe POST with retry + timing logic
📁 Project Structure
tdsp22/
│
├── agent.py              # LangGraph agent definition
├── main.py               # FastAPI server (entrypoint)
├── shared_store.py       # Shared runtime storage (base64, timers)
│
├── requirements.txt      # Python dependencies
├── Dockerfile            # HuggingFace Spaces Docker config
│
├── README.md             # Project documentation
└── LICENSE               # MIT License

🔥 How the System Works
1️⃣ TDS Server → Your /solve Endpoint

Example incoming payload:

{
  "email": "your-email",
  "secret": "your-secret",
  "url": "https://example.com/quiz-834"
}

2️⃣ Your server verifies:

JSON validity

Secret correctness

Required fields

3️⃣ Agent starts solving the quiz

The agent will:

Fetch the quiz page

Render JavaScript if needed

Extract data

Solve the task (code execution, analysis, OCR, etc.)

Prepare answer JSON

Submit to the submit endpoint defined inside the page

4️⃣ Server Response Handling

If:

correct: true + url: next-quiz-url → continue solving

correct: false + within 3 minutes → retry

No next URL → finish

All logic respects TDS timing rules:
3-minute absolute timeout per quiz.

🐳 Deployment (Hugging Face Spaces – Docker)

This Space is deployed using a custom Dockerfile with:

Python 3.10 slim-bookworm

Playwright Chromium + dependencies

Tesseract OCR

FFmpeg

All requirements installed via uv --system

The server runs automatically:

uv run main.py


Your public API endpoint becomes:

https://<username>-<space-name>.hf.space/solve

▶️ Running Locally
1. Create environment
uv venv
uv pip install -r requirements.txt

2. Run Playwright (first time only)
playwright install chromium

3. Start API
uvicorn main:app --host 0.0.0.0 --port 7860

🔑 Environment Variables

Create .env:

EMAIL=your-email
SECRET=your-secret
GOOGLE_API_KEY=your-gemini-api-key

🧪 Health Check
GET /healthz


Response:

{
  "status": "ok",
  "uptime_seconds": 123
}

📬 Solve Endpoint
POST /solve


Example:

{
  "email": "your-email",
  "secret": "your-secret",
  "url": "https://tds-llm-analysis.s-anand.net/demo"
}


Response:

{
  "status": "ok"
}


The solving runs asynchronously.

📜 License

This project is licensed under the MIT License.
