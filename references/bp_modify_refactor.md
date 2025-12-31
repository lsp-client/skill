# Best Practice Scenario: Refactoring a Legacy Function

This scenario demonstrates how to combine LSAP capabilities to safely refactor code.

## Scenario
You are tasked with refactoring `process_transaction` in `src/payments.py`.

## Workflow

### 1. Survey the Territory
First, understand the context of the file.

```bash
lsp outline src/payments.py
```

**Why**: Check if there are private helper functions or shared constants you need to be aware of.

### 2. Understand the Logic
Read the function's implementation details.

```bash
lsp definition src/payments.py --line 50 --find "def process_transaction" --code
```

**Why**: Get the source code to analyze the current logic.

### 3. Assess Impact (The Safety Check)
Before changing anything, see who calls this function.

```bash
lsp reference src/payments.py --line 50 --find "def process_transaction" --context-lines 2
```

**Why**: The `--context-lines` flag shows you *how* it's being called (e.g., arguments passed) without needing to open every file.

### 4. Verify Types
Check types of specific variables inside the function if unclear.

```bash
lsp hover src/payments.py --line 55 --find "user_id"
```

**Why**: Ensure you don't violate type constraints during refactoring.
