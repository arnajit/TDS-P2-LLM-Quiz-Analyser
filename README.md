# TDS-P2-LLM-Quiz-Analyser

TDS-P2-LLM-Quiz-Analyser is a tool for analyzing multiple-choice quizzes using Large Language Models (LLMs). It helps educators and content creators automatically grade quizzes, provide item-level analysis (difficulty, discrimination), generate feedback and distractors, and surface insights about student performance and question quality.

This README provides an overview, quickstart instructions, expected data formats, example usage, and guidance for contribution.

## Features

- Auto-grade multiple-choice quizzes from structured quiz files.
- Per-question analysis: difficulty estimate, discrimination index, and flagged ambiguous items.
- Natural-language feedback generation for each student response.
- Optionally generate improved distractors and alternative phrasings using an LLM.
- Export results to CSV / JSON for reporting and visualization.
- Extensible: supports different LLM providers (OpenAI, local models) via a config layer.

## Who is this for?

- Teachers and instructional designers who want faster item analysis.
- Researchers analyzing quiz quality and student performance.
- Developers building LLM-assisted assessment tooling.

## Quick Start

1. Clone the repository:
   git clone https://github.com/arnajit/TDS-P2-LLM-Quiz-Analyser.git
   cd TDS-P2-LLM-Quiz-Analyser

2. Create and activate a virtual environment (Python example):
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure your LLM provider credentials (example uses OpenAI):
   export OPENAI_API_KEY="sk-..."

5. Run the analyser on a quiz file:
   python -m tds_quiz_analyser.cli analyze --input examples/sample_quiz.json --output results/report.json

Note: Commands above are examples — adapt to the actual CLI/module names in the repository.

## Installation

The repository supports running directly from source. If a package distribution is provided, install with pip:

pip install .

Or, for development:

pip install -e .

## Configuration

The analyser can be configured through environment variables or a config file (e.g., `config.yaml`). Typical configuration settings:

- LLM provider (openai, local, etc.)
- API key or credentials (e.g., OPENAI_API_KEY)
- Model name (gpt-4, gpt-3.5-turbo, local-llm)
- Analysis options (generate_feedback: true/false, generate_distractors: true/false)
- Output formats (json, csv)

Example environment variable:
export OPENAI_API_KEY="sk-..."

Example `config.yaml`:
```yaml
llm:
  provider: openai
  model: gpt-4
  temperature: 0.2
analysis:
  generate_feedback: true
  generate_distractors: false
output:
  formats: ["json","csv"]
```

## Data format

Input quiz files should be structured JSON (or CSV) describing the quiz, questions, choices, and student responses. Example JSON schema:

{
  "quiz_id": "quiz-001",
  "title": "Intro to Biology - Quiz 1",
  "questions": [
    {
      "id": "q1",
      "text": "What is the powerhouse of the cell?",
      "choices": [
        {"id":"a","text":"Nucleus"},
        {"id":"b","text":"Mitochondria"},
        {"id":"c","text":"Ribosome"},
        {"id":"d","text":"Golgi apparatus"}
      ],
      "correct_choice_id": "b"
    }
  ],
  "responses": [
    {
      "student_id": "s1",
      "answers": [
        {"question_id":"q1","choice_id":"a"}
      ]
    }
  ]
}

Adjust field names as needed by your local data pipeline. The repo includes example input files in `examples/`.

## Usage

CLI (example):
- Analyze a quiz:
  python -m tds_quiz_analyser.cli analyze --input path/to/quiz.json --output path/to/report.json

- Run analysis with custom config:
  python -m tds_quiz_analyser.cli analyze --input quiz.json --config config.yaml

Python API (example):
from tds_quiz_analyser import QuizAnalyser, load_quiz
quiz = load_quiz("examples/sample_quiz.json")
analyser = QuizAnalyser(config={"llm": {"provider": "openai", "model": "gpt-4"}})
report = analyser.run(quiz)
print(report.to_json())

Outputs typically include:
- per-student grading (score, correct/incorrect)
- per-question statistics (p-value/difficulty, discrimination index)
- flagged items (ambiguous or low-quality distractors)
- generated feedback (if enabled)
- optional recommended alternative distractors or rewrite suggestions

## Examples

Look in the `examples/` folder for:
- sample_quiz.json — a minimal quiz and response set
- run_examples.sh — example commands to run the analyser

## Testing

Run tests with pytest:
pytest

If tests require network access to the LLM provider, consider using recorded responses or mocks (see tests/fixtures).

## Development

- Use a virtual environment and keep dependencies in `requirements.txt`.
- Linting and formatting: run flake8 / black if configured.
- When adding new LLM providers, implement the provider interface in `tds_quiz_analyser/llm_providers/`.

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repository.
2. Create a feature branch: git checkout -b feat/your-feature
3. Add tests and documentation.
4. Submit a pull request describing your change.

Please follow the repository's code style and include tests for new features.

## Security and Privacy

- Do not commit API keys or sensitive student data. Use environment variables or secure vaults for secrets.
- Ensure any student data you analyze complies with applicable privacy regulations (e.g., FERPA, GDPR).

## Roadmap / Ideas

- Support for adaptive quizzes and item-response theory (IRT) analysis.
- Integration with LMS platforms (Canvas, Moodle).
- Web frontend for interactive reports and per-student dashboards.
- Batch processing and streaming ingestion for large-scale deployments.

## Troubleshooting

- If the analyser fails to contact the LLM provider, verify API key and network connectivity.
- For unexpected analysis results, review the raw response logs (if enabled) and sample inputs.

## License

Specify the license for this repository (e.g., MIT). Update LICENSE file accordingly.

## Contact

Maintainer: arnajit
GitHub: https://github.com/arnajit/TDS-P2-LLM-Quiz-Analyser

---

If you'd like, I can:
- tailor the README to the repository's actual language and CLI names by inspecting the code, or
- open a README.md file commit in the repository for you.

Tell me which you'd prefer and I will proceed.
