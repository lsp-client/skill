# AGENTS.md

## Development Commands

- Lint & format: `ruff check --fix && ruff format`
- Type checking: `ty check <dir_or_file>`
- Run tests: `uv run pytest`
- Sync latest deps: `uv sync --upgrade`

## Code Style Guidelines

- Python: 3.13+ required
- `attrs` for class definitions
- `anyio` and `asyncer` for async programming
- `typer` for cli, `rich` for printing
