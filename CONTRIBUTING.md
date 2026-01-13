# Contribution Guide

## Core Principles

- **Conciseness**: Only add what an LLM agent needs. Avoid fluff.
- **LSAP Alignment**: Follow Language Server Agent Protocol principles (progressive disclosure, high-density context).
- **Verification**: Test CLI commands before documenting them.

## Development Setup

We use `uv` for dependency management. Please ensure you have it installed.

1.  **Sync dependencies**:
    ```bash
    uv sync
    ```

2.  **Run the CLI in development**:
    ```bash
    uv run lsp --help
    ```

## Development Workflow

### Code Style & Quality

We maintain high standards for code quality and type safety:

- **Formatting & Linting**: We use `ruff`.
  ```bash
  just lint
  ```
- **Type Checking**: We use `ty check`.
  ```bash
  just check
  ```
- **Testing**: We use `pytest`.
  ```bash
  just test
  ```

### Adding New Commands

`lsp-cli` uses `typer` for its command-line interface. Commands are defined in `src/lsp_cli/__main__.py`.

1.  Define the command using `@app.command()`.
2.  Use the `Annotated` pattern for arguments and options (see `src/lsp_cli/options.py`).
3.  Ensure the command uses the `init_client` context manager to interact with the background manager.
4.  Format the output using `rich`.

### Improving the Manager

The background manager is located in `src/lsp_cli/manager/`. It uses `litestar` to provide a UDS-based API for managing LSP clients.

## Best Practices Structure

Best practices are organized in `skills/lsp-code-analysis/references/` with hierarchical naming:

```
skills/lsp-code-analysis/references/
├── bp_<category>.md               # Category guides (explore, modify, troubleshoot)
├── bp_<category>_<scenario>.md    # Specific scenarios
└── bp_<lang>_<domain>.md          # Language/domain specific
```

### Naming Convention

| Pattern                       | Use Case                    | Example                                         |
| ----------------------------- | --------------------------- | ----------------------------------------------- |
| `bp_<category>.md`            | General category guide      | `bp_explore.md`                                 |
| `bp_<category>_<scenario>.md` | Specific scenario           | `bp_modify_refactor.md`                         |
| `bp_<lang>_<domain>.md`       | Language or domain specific | `bp_python_django.md`, `bp_typescript_react.md` |

### Adding a New Best Practice

```bash
# Initialize from template
just new-bp <category> [scenario]

# Examples:
just new-bp explore                  # -> bp_explore.md
just new-bp modify api-migration     # -> bp_modify_api-migration.md
just new-bp python django            # -> bp_python_django.md
```

Then add an entry to the appropriate table in `skills/lsp-code-analysis/SKILL.md` or domain indices.

### Current Categories

- `explore` — Understanding/navigating code
- `modify` — Changing/refactoring code
- `troubleshoot` — Fixing LSP issues

## Testing Changes

1. Verify `lsp` commands work as described
2. Run project tests: `just test`
3. Repackage: `just package`
