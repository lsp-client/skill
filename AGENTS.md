# AGENTS.md

## Project Structure

```
├── SKILL.md              # Skill definition (for agents using this skill)
├── CONTRIBUTING.md       # Contribution guide (for developers)
├── references/
│   ├── bp.md             # Best practices index (decision tree)
│   ├── bp_*.md           # Best practice guides
│   ├── bp_template.md    # Template for new best practices
│   └── lsap.md           # Protocol reference
└── justfile              # Developer commands
```

## Common Tasks

### Adding a New Best Practice

1. Run `just new-bp <category> [scenario]` to create from template
2. Edit the generated file in `references/`
3. Add entry to the appropriate table in `references/bp.md`
4. Verify naming follows convention in `CONTRIBUTING.md`

### Modifying SKILL.md

- Keep under 100 lines; move details to `references/`
- `description` in frontmatter must contain all trigger conditions

### Modifying bp.md

- This is the agent-facing index; keep it minimal
- Use tables for quick scanning
- Do not add developer instructions here (use CONTRIBUTING.md)

## Quality Checks

Before completing a contribution:

- [ ] CLI commands in examples are valid (`lsp <cmd> --help` to verify)
- [ ] New `bp_*.md` files follow `bp_template.md` structure
- [ ] `references/bp.md` updated if adding new best practice
- [ ] No developer-facing content in agent-facing files
