# Contribution Guide for lsp-analysis Skill

## Core Principles

- **Conciseness**: Only add what an LLM needs to know. Avoid fluff.
- **LSAP Alignment**: Ensure new instructions follow the Language Server Agent Protocol principles (progressive disclosure, high-density context).
- **Verification**: Test any recommended CLI commands or patterns before adding them.

## Adding Best Practices

1. Open `references/best_practices.md`.
2. Add a new section under "Extensible Best Practices".
3. Use concise bullet points or short examples.

## Adding Reference Material

- If adding a complex capability (e.g., `call-hierarchy`), create a new file in `references/` (e.g., `references/call_hierarchy.md`).
- Link to it from `SKILL.md` under the "References" section.

## Workflow Updates

- Only update the main workflow in `SKILL.md` if the change is fundamental to all users of the skill.
- Prefer adding task-specific workflows to `references/best_practices.md`.

## Testing Changes

1. Run `lsp-cli` commands manually to verify they work as described.
2. Repackage the skill using:
   `uv run --with pyyaml /path/to/skill-creator/scripts/package_skill.py <skill_dir>`
