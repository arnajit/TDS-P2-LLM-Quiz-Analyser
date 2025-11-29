# TDS-P2-LLM-Quiz-Analyser

A lightweight toolkit to analyze multiple-choice quiz data using Large Language Models (LLMs). This project provides utilities to parse quiz results, run LLM-based analysis (insights, difficulty estimation, distractor quality), and export human-readable reports and visualizations.

> NOTE: This README is a general, ready-to-use guide. Adjust the commands and entry points to match the actual files in the repository (for example `main.py`, `app.py`, or the notebooks/CLI that exist here).

## Table of contents
- Overview
- Key features
- Project structure
- Requirements
- Installation
- Quick start
- Usage examples
- Configuration
- Contributing
- Troubleshooting
- Acknowledgements
- License

## Overview
The TDS-P2-LLM-Quiz-Analyser helps instructors, item-writers, and course teams understand quiz performance by combining classical item analysis (e.g., p-values, discrimination indices) with LLM-powered qualitative analysis (explain correctness, identify misleading distractors, suggest improvements). The tool can be used locally or integrated into pipelines that process quiz CSVs and produce reports.

## Key features
- Parse common quiz/export formats (CSV).
- Compute classical psychometric statistics (difficulty, discrimination).
- Ask an LLM to:
  - Explain correct answers in plain language.
  - Evaluate distractor plausibility and suggest improvements.
  - Generate short feedback to students for each option.
- Output:
  - CSV/JSON reports with metrics and LLM responses.
  - Optional human-friendly HTML or Markdown summary report.
  - (Optional) Visualizations for item-level and test-level metrics.

## Project structure (example)
- data/ — sample quiz files and format examples
- src/ or app/ — core analyzer code and helpers
- notebooks/ — exploratory analysis and demos (if present)
- scripts/ — convenience scripts (CLI wrappers, export scripts)
- requirements.txt — Python dependencies
- README.md — this file

Adjust this section to match the actual repo layout.

## Requirements
- Python 3.9+ (or the version used in the project)
- pip
- An OpenAI-compatible LLM API key or other supported LLM provider credentials if using LLM features
- Recommended: virtualenv or venv

## Installation (local)
1. Clone the repo:
   git clone https://github.com/arnajit/TDS-P2-LLM-Quiz-Analyser.git
   cd TDS-P2-LLM-Quiz-Analyser

2. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows

3. Install dependencies:
   pip install -r requirements.txt

If the repo uses Poetry or Pipenv, use the appropriate commands (e.g., `poetry install`).

## Quick start
1. Prepare a CSV of quiz responses. Expected columns (example):
   - question_id, question_text, option_a, option_b, option_c, option_d, correct_option, student_id, student_answer

2. Run the analyzer (example placeholders — replace with actual script name):
   python src/analyze_quiz.py --input data/sample_quiz.csv --output reports/summary.json

3. To enable LLM analysis, set your LLM API key in the environment:
   export OPENAI_API_KEY="sk-..."
   # or for windows:
   setx OPENAI_API_KEY "sk-..."

4. Include an LLM flag if needed:
   python src/analyze_quiz.py --input data/sample_quiz.csv --output reports/ --use-llm

If this project exposes a different CLI or a notebook, run that instead (e.g., `jupyter notebook notebooks/demo.ipynb`).

## Usage examples
- Generate a JSON report:
  python src/analyze_quiz.py --input data/class_quiz.csv --output reports/class_quiz_report.json

- Generate a markdown summary and HTML visualization:
  python src/analyze_quiz.py --input data/class_quiz.csv --output reports/ --format markdown,html

- Run only the classical psychometric analysis (no LLM):
  python src/analyze_quiz.py --input data/class_quiz.csv --output reports/ --no-llm

## Configuration
- Environment variables:
  - OPENAI_API_KEY (or other provider-specific key)
  - ANALYZER_MODEL (optional — set default LLM model to use)
- Config file (optional): config.yml (example):
  model: gpt-4o-mini
  max_tokens: 400
  llm_timeout: 30
  output_formats: [json, markdown]

If the repository includes a config schema or examples, adapt the above to match it.

## Extending the project
- Add new LLM prompts tailored to your discipline for better feedback.
- Add support for more input formats (Moodle XML, LMS exports).
- Add automated unit tests for the analysis metrics and LLM response parsing.
- Containerize with Docker for reproducible runs in CI.

## Contributing
Contributions are welcome:
- Fork the repo and create a feature branch.
- Add tests for new behavior.
- Open a PR with a clear description of the change.
- Follow the project's coding style and testing practices.

Suggested git workflow to add this README:
git checkout -b docs/add-readme
git add README.md
git commit -m "chore: add project README"
git push origin docs/add-readme
Then open a Pull Request on GitHub.

## Troubleshooting
- LLM requests failing: check API key, provider limits, network connectivity.
- Incorrect metrics: verify your input CSV conforms to the expected schema and there are no missing/invalid answers.
- Performance: process very large quizzes in batches or use streaming LLM APIs (if available).

## Acknowledgements
- Built for the TDS Project 2 coursework.
- Powered by open LLM APIs (configure provider of your choice).

## License
MIT license is also genrated for the project
