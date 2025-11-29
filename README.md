# TDS-P2-LLM-Quiz-Analyser

A toolkit for analyzing quiz content and responses using large language models (LLMs). This project provides components to ingest quizzes, run automated analyses (difficulty, topic coverage, distractor quality, grading and feedback generation), and produce human-readable reports to help instructors and content authors improve quizzes.

> Note: This README is intentionally generic and written to be easily adapted. If you want the usage examples or script names tailored to the repository's actual entry points, tell me which files to reference and I'll update it.

## Features

- Ingest quiz datasets (CSV, JSON, or similar formats).
- Use LLMs to:
  - Assess question difficulty and clarity.
  - Tag questions by topic and learning objective.
  - Evaluate distractor quality for multiple-choice items.
  - Generate graded feedback and suggested improvements.
- Output structured reports (JSON/CSV) and human-friendly summaries.
- Configurable model/provider integration (OpenAI, Anthropic, local models).
- Modular codebase for easy extension and experimentation.

## Who is this for?

- Instructional designers and educators who want automated insights on quiz quality.
- Developers building educational tooling that needs automatic analysis and labeling.
- Researchers exploring automated question analysis using LLMs.

## Repository layout

This project follows a modular layout (adjust to actual paths in the repo as needed):

- data/                     - Example input files and sample exports
- src/                      - Core application logic and modules
  - ingestion/              - Parsers for CSV/JSON quiz formats
  - llm/                    - Model adapters, prompts, and response parsing
  - analysis/               - Scoring logic, metrics, and heuristics
  - reporting/              - Report generation (JSON, CSV, HTML)
  - cli.py                  - Command-line entry point
- tests/                    - Unit and integration tests
- docs/                     - Additional docs and design notes
- requirements.txt          - Python dependencies (if applicable)

(If your repository layout differs, update this section to reflect the actual structure.)

## Quickstart

Prerequisites:
- Python 3.8+ (if this is a Python project) or the appropriate runtime for your implementation.
- pip and virtualenv (or conda), or another language's package manager.
- An API key for your chosen LLM provider (e.g., OPENAI_API_KEY) if using hosted models.

Basic setup (Python example):

1. Clone the repository
   git clone https://github.com/arnajit/TDS-P2-LLM-Quiz-Analyser.git
   cd TDS-P2-LLM-Quiz-Analyser

2. Create and activate a virtual environment
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Set environment variables
   export OPENAI_API_KEY="sk-..."         # macOS/Linux
   setx OPENAI_API_KEY "sk-..."           # Windows (or use your shell)

5. Run an analysis (example placeholder)
   python src/cli.py analyze --input data/sample_quizzes.csv --output reports/report.json

Notes:
- Replace the CLI command above with the actual entry point in the repository (e.g., `python src/main.py`, or a package/module invocation).
- If you use another LLM provider or local model, configure the provider adapter in the config file or environment variables.

## Usage examples

Example: Analyze a quiz file and generate a JSON report
- Input: data/sample_quizzes.csv
- Output: reports/sample_analysis.json

Command (placeholder):
python src/cli.py analyze \
  --input data/sample_quizzes.csv \
  --model openai/gpt-4 \
  --output reports/sample_analysis.json \
  --topics --difficulty --distractors --feedback

Example: Generate an HTML summary for instructors
python src/cli.py summarize --report reports/sample_analysis.json --format html --out reports/summary.html

Adjust flags and module names to match the repository's actual CLI API.

## Configuration

Common configuration options (implement as environment variables or config file):
- MODEL_PROVIDER (e.g., openai, anthropic, local)
- MODEL_NAME (e.g., gpt-4, gpt-4o, claude-2)
- OPENAI_API_KEY (or provider-specific keys)
- MAX_TOKENS, TEMPERATURE, RETRIES
- DEFAULT_OUTPUT_FORMAT (json/csv/html)
- PROMPT_TEMPLATES_DIR (path to prompt templates)

## Architecture & Design Notes

- Prompting: Keep prompts modular and maintain templates in a dedicated directory so tests and improvements are easy to apply.
- Safety: Sanitize input content and be mindful of exposing student data to third-party APIs. Consider on-prem models for sensitive data.
- Extensibility: Provide a clear adapter interface for new model providers and for alternate analysis heuristics.

## Metrics & Evaluation

- Suggested automated metrics to compute:
  - Question difficulty distribution (easy / medium / hard)
  - Topic coverage (questions per learning objective)
  - Distractor quality score (for MCQs)
  - Estimated discrimination index and reliability (if student-response data available)

- Collect human validation samples to calibrate thresholds and prompt templates for your domain.

## Development

- Run tests:
  pytest -q

- Run linting and formatting:
  black .
  flake8

- Add new LLM adapters by implementing the adapter interface in src/llm/

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repository.
2. Create a feature branch: git checkout -b feat/your-feature
3. Add tests and documentation.
4. Open a pull request describing your changes and the motivation.

Please follow the existing coding and documentation style. If you plan a large change, open an issue first to discuss the design.

## Examples and sample data

- data/sample_quizzes.csv — sample input format (questions, options, correct answers, metadata)
- reports/ — example outputs generated by the analysis pipeline

If sample files are not present, create a small CSV with columns such as:
id, question, option_a, option_b, option_c, option_d, correct_option, topic, difficulty_manual

## Troubleshooting

- If you see API rate limits: reduce concurrency, add retries/backoff, or switch to a higher-tier model.
- If outputs are inconsistent: stabilize prompts, add system-level instructions, and use few-shot examples.

## License

Specify the project license (e.g., MIT). If none is present, add a LICENSE file to the repository.

## Contact

Maintainer: arnajit
Repository: https://github.com/arnajit/TDS-P2-LLM-Quiz-Analyser

---

If you want, I can:
- Tailor the Usage section to exact script/module names found in the repo (point me to the CLI or main scripts).
- Add badges (build, license, coverage).
- Generate a minimal sample dataset and a demo command that runs end-to-end. Which would you prefer next?
