# Test Fixtures

This directory contains minimal test projects for each supported language in LSP CLI.

## Purpose

These fixtures are used by the language support tests (`test_language_support.py`) to verify that LSP CLI can correctly:
- Detect and start language servers for each supported language
- Manage server lifecycle (start, list, stop)
- Handle multiple language servers simultaneously

## Structure

Each subdirectory contains a minimal but valid project for its respective language:

- **go_project/**: Go project with `go.mod` and simple main package
- **rust_project/**: Rust project with `Cargo.toml` and src directory
- **typescript_project/**: TypeScript project with `package.json`, `tsconfig.json`, and TypeScript file
- **javascript_project/**: JavaScript project with `package.json` and ES module
- **deno_project/**: Deno project with `deno.json` configuration

## Requirements

For the tests to work, the following language servers must be installed:
- `basedpyright` (Python)
- `gopls` (Go)
- `rust-analyzer` (Rust)
- `typescript-language-server` (TypeScript/JavaScript)
- `deno` (Deno)

However, the tests will skip or fail gracefully if the required language server is not installed or cannot be started for a project.

## Maintenance

These fixtures should remain minimal and focused. They exist only to verify basic LSP server integration, not to test language-specific features.
