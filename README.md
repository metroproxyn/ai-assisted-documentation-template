# AI-Assisted Documentation Template

This repository demonstrates how AI can be integrated into a documentation workflow. It uses GitHub Actions and LLMs to automatically suggest documentation updates when code or API specs change.

## Features
- **Structured Prompts Library**: A curated collection of LLM prompts designed to scale with your expertise.
  - (prompts-core.md)[prompts-core.md] - A solid foundation for everyday technical writing tasks: drafting, editing, and research.
  - (`prompts-advanced.md`)[prompts-advanced.md] - For senior-level challenges: information architecture, accuracy validation, audience adaptation, and process automation.
- **GitHub Action** (`auto-docs-update.yml`) that detects changes in code/specs and generates draft documentation updates
- **AI Update Script** (`ai_doc_update.py`) that calls an LLM API and produces Markdown suggestions
- **Pull Request Template** to guide reviewers and ensure AI outputs are verified

## Workflow
1. Developer pushes code changes (e.g., in `openapi.yaml`).
2. GitHub Action runs `ai_doc_update.py`.
3. The script generates `AI_DOC_UPDATE.md` with suggested doc changes.
4. An automated PR is created with the suggested updates.
5. Reviewer checks accuracy, tone, and compliance using the PR checklist.

## Setup
1. Add your LLM API key as a GitHub secret (`OPENAI_API_KEY`).
2. Push changes to the repo.
3. When relevant files are updated, the workflow will run and create a PR.

>‼️**Important**: All AI-generated outputs require human-in-the-loop validation before applying its results into the documentation.