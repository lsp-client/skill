# Best Practice: Exploration Strategy

## The "Map then Territory" Strategy

Before diving into specific functions, always build a mental map of the file or module.

*   **Action**: Use `lsp outline <file>` immediately after opening or identifying a relevant file.
*   **Why**: This provides a high-level AST summary (classes, methods, variables) without flooding the context with implementation details. It helps you decide *where* to look next.

## Broad to Narrow Discovery

When exploring a new codebase, follow this funnel:

1.  **Workspace Search**: `lsp symbol "Query"` to find entry points across the project.
2.  **File Map**: `lsp outline path/to/file.py` to understand the structure of the found file.
3.  **Deep Inspection**: `lsp definition ...` or `lsp hover ...` to understand specific logic.
4.  **Relational Check**: `lsp reference ...` to see how the code is used elsewhere.
