# Best Practice: Robust Locating

## Anchor with Text, Not Just Lines

Line numbers are fragile. If code changes above your target, the line number shifts.

*   **Bad**: `lsp definition main.py --line 50`
*   **Good**: `lsp definition main.py --line 50 --find "def process_data"`

## Why It Matters

The `--find` argument acts as a semantic anchor. If `process_data` moved to line 52, LSAP will likely still find it near line 50 because it searches for the text snippet in the vicinity of the provided line.

Always include a unique snippet of the symbol definition or usage you are targeting.
