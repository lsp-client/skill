# AGENTS.md

## Project Structure

```
├── skills/
│   └── lsp-code-analysis/    # Main skill directory
│       ├── SKILL.md          # Skill definition
│       ├── references/       # Best practice guides (bp_*.md)
│       └── assets/           # Templates and assets
├── lib-references/           # External library/protocol references
│   ├── LSAP/                 # LSAP protocol source
│   └── lsp-cli/              # lsp-cli source
├── CONTRIBUTING.md           # Development guide
└── justfile                  # Development commands
```

## Common Tasks

### Adding a New Best Practice

1. Run `just new-bp <category> [scenario]` to create from template
2. Edit the generated file in `skills/lsp-code-analysis/references/`
3. Add entry to the appropriate index in `SKILL.md` or domain `bp_*.md` file
4. Verify naming follows convention in `CONTRIBUTING.md`

### Modifying SKILL.md

- Keep content minimal; move details to `references/`
- `description` in frontmatter must contain all trigger conditions

### Modifying bp\_\*.md

- Keep agent-facing indices minimal
- Use tables for quick scanning
- Do not add developer instructions here (use CONTRIBUTING.md)

## Quality Checks

Before completing a contribution:

- [ ] CLI commands in examples are valid (`lsp <cmd> --help` to verify)
- [ ] New `bp_*.md` files follow `bp_template.md` structure
- [ ] No developer-facing content in agent-facing files

