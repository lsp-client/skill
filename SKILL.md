---
name: lsp-code-analysis
description: High-fidelity code analysis using Language Server Protocol. Use this skill when you need to:(1) Navigate to function/class definitions, (2) Understand file structure via outline, (3) Find all usages of a symbol across the codebase, (4) Search for classes/functions by name globally, (5) Get documentation and type signatures. Ideal for code exploration, impact analysis, refactoring preparation, and understanding unfamiliar codebases.
---

# LSP Code Analysis

Leverage language server intelligence for precise code navigation and understanding. This skill uses the Language Server Agent Protocol (LSAP), designed for agent-friendly code analysis with progressive disclosure and robust symbol locating.

For protocol details, see [references/lsap.md](references/lsap.md).

## Prerequisites

```bash
uv tool install lsp-cli
```

## Commands

All commands support `-h` or `--help` for detailed argument documentation.

### The `--scope` Parameter

Most analysis commands use `--scope` (or `-s`) to narrow down the search area within a file. It is highly flexible:

- **Line Number**: `--scope 42` (Search at or near line 42)
- **Line Range**: `--scope 10,50` (Search between line 10 and 50)
- **Symbol Path**: `--scope User.profile.update` (Search within a specific class or function hierarchy)

### Outline: Understand File Structure

**Guidance:** ALWAYS use this before reading a file. It provides a structural map that helps you identify relevant sections. **Prefer `outline` over full file `read`** for non-essential code to save tokens and maintain high-level focus.

```bash
lsp outline <file_path>
```

### Definition: Navigate to Source

**Guidance:** Use to quickly jump to dependencies or implementation details. When tracking complex logic, use `definition` to verify function signatures and return types without reading the entire callee file.

```bash
# Locate by symbol path
lsp definition src/models.py --scope User.get_id
# Locate by line and text anchor
lsp definition src/main.py --scope 10 --find "process_data"
```

### Reference: Find All Usages

**Guidance:** Mandatory before refactoring or deleting code. Use the `implementations` mode to find concrete logic in interface-heavy or abstract codebases.

```bash
# Find references within a specific function
lsp reference src/main.py --scope MyClass.run --find "logger"
# Find concrete implementations of an interface
lsp reference src/api.py --find "IDataProvider" --mode implementations
```

### Search: Global Symbol Search

**Guidance:** Use for "lost in codebase" scenarios. Combine with `--kind` to filter out noise (e.g., finding a `class` when many functions have similar names).

```bash
# Fuzzy search for symbols
lsp search "MyClassName" <project_root>
# Filter by kind (class, function, method, etc.)
lsp search "init" . --kind function --kind method
```

### Symbol: Local Symbol Info

**Guidance:** Use to resolve ambiguity in dense code. It provides precise location data that can be used to anchor subsequent `hover` or `definition` calls.

```bash
lsp symbol src/main.py --find "my_variable"
```

### Hover: Get Documentation

**Guidance:** **Prefer `hover` over `read`** to understand how to call a function or use a class. It returns docstrings and type signatures, giving you the "API contract" without the "implementation noise."

```bash
lsp hover src/main.py --find "my_function"
```

## Best Practices

Leverage these structural exploration workflows to quickly complete project analysis in specific scenarios. These guides help you navigate codebases efficiently without reading every line.

Refer to each scenario's index file for detailed best practices.

- Frontend: [bp_frontend.md](references/bp_frontend.md)
- Backend: [bp_backend.md](references/bp_backend.md)
