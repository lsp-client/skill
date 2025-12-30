# Best Practice: Efficient Inspection

## Understanding Context

When using `reference`, leverage the context options to understand usage without reading every file.

*   **Action**: Use `lsp reference ... --context-lines 2`
*   **Why**: This gives you the surrounding code for each usage site, often answering "how is this used?" without needing to open the consuming file.

## Server Management

The `lsp-cli` manages background servers automatically. You do not need to manually start/stop servers for each command.

*   **Tip**: Group your queries. The first request starts the server (which may take a moment). Subsequent requests to the same project are instant.
