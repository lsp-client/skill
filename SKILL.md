---
name: lsp-code-analysis
description: High-fidelity code analysis using Language Server Protocol. Use this skill when you need to:(1) Navigate to function/class definitions, (2) Understand file structure via outline, (3) Find all usages of a symbol across the codebase, (4) Search for classes/functions by name globally, (5) Get documentation and type signatures. Ideal for code exploration, impact analysis, refactoring preparation, and understanding unfamiliar codebases.
---

# LSP Code Analysis

Leverage language server intelligence for precise code navigation and understanding. This skill uses the **Language Server Agent Protocol (LSAP)**, designed for agent-friendly code analysis with progressive disclosure and robust symbol locating.

For protocol details, see [references/lsap.md](references/lsap.md).

## Prerequisites

```bash
uv tool install lsp-cli
```

## Commands

### Outline: Understand File Structure

Start here when exploring a new file. Get a structural map of classes, methods, and functions.

```bash
lsp outline <file_path>
```

### Definition: Navigate to Source

Jump to where a symbol is defined. Use `--find` to anchor to text (handles line number drift).

```bash
lsp definition src/main.py --line 10 --find "process_data"
```

### Reference: Find All Usages

Discover everywhere a symbol is used. Essential for impact analysis before changes.

```bash
lsp reference src/main.py --line 10 --find "User"
```

Options: `--mode implementations` for interface implementations.

### Symbol: Global Search

Find classes/functions by name across the entire project (fuzzy search).

```bash
lsp symbol "SymbolName" <project_root>
```

### Hover: Get Documentation

Retrieve docstrings and type signatures without leaving context.

```bash
lsp hover src/main.py --line 10 --find "my_function"
```

## Best Practices

### General

### Scenario

- Frontend: [bp_frontend.md](references/bp_frontend.md)
- Backend: [bp_backend.md](references/bp_backend.md)
