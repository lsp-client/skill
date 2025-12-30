---
name: lsp-analysis
description: Analyze code using the LSP CLI and Language Server Agent Protocol (LSAP). Use this skill to find definitions, references, symbols, and code structure.
---

# LSP Analysis

This skill provides tools to analyze codebases using the `lsp-cli`, which leverages the **Language Server Agent Protocol (LSAP)** for high-fidelity, agent-friendly code intelligence.

## When to Use

Use this skill when you need to:
1.  **Understand Code**: Find where a function or class is defined (`definition`).
2.  **Explore Structure**: Get a high-level map of a file (`outline`).
3.  **Find Usage**: See everywhere a symbol is used (`reference`).
4.  **Search Global Symbols**: Find classes/functions by name across the project (`symbol`).
5.  **Get Details**: Read documentation and signatures (`hover`).

## Core Concepts

LSAP is designed for agents. It prioritizes **Progressive Disclosure** and **Robust Locating**.
For a deeper understanding of the protocol, see [references/lsap.md](references/lsap.md).

## Prerequisites

This skill requires the [lsp-cli](https://github.com/lsp-client/lsp-cli) tool to be installed in the environment where the agent runs.

```bash
uv tool install lsp-cli
```

## CLI Usage

The `lsp` command is your primary interface. It automatically manages language servers in the background.

### 1. File Outline (Start Here)

Get a structural map of a file to understand its classes and methods.

```bash
lsp outline <file_path>
```

### 2. Find Definition

Go to the definition of a symbol. **Crucially**, use `--find` to anchor your request to a text snippet.

```bash
# Syntax: lsp definition <file> --line <approx_line> --find "<unique_snippet>"
lsp definition src/main.py --line 10 --find "process_data"
```

*   `--line`: Approximate line number (helps disambiguate).
*   `--find`: The text of the symbol you are interested in.
*   `--code`: (Default: True) Includes the source code of the definition.

### 3. Find References

Find all usages of a symbol in the workspace.

```bash
lsp reference src/main.py --line 10 --find "User"
```

*   `--mode`: `references` (default) or `implementations`.

### 4. Workspace Symbol Search

Search for a symbol by name across the entire project (fuzzy search).

```bash
lsp symbol "SymbolName" <project_root>
```

### 5. Hover & Documentation

Get documentation strings and type signatures.

```bash
lsp hover src/main.py --line 10 --find "my_function"
```

## Best Practices

Select the appropriate guide for your current needs:

- **Strategic Exploration**: [references/bp_exploration_strategy.md](references/bp_exploration_strategy.md)
  *   Use when entering a new codebase or file. Covers "Map then Territory" and the "Broad to Narrow" discovery funnel.

- **Robust Locating**: [references/bp_robust_locating.md](references/bp_robust_locating.md)
  *   **CRITICAL**: Read this if your LSP requests are failing or missing targets. Explains how to use text anchors (`--find`) to handle shifting line numbers.

- **Efficient Inspection**: [references/bp_efficient_inspection.md](references/bp_efficient_inspection.md)
  *   Tips for maximizing information per query (context lines) and understanding server lifecycle management.

- **Example Workflow**: [references/bp_scenario_refactoring.md](references/bp_scenario_refactoring.md)
  *   A concrete walkthrough of investigating and refactoring a function using multiple LSP commands.



