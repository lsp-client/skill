# Initialize a new best practice file
# Usage: just new-bp <category> [scenario]
# Examples:
#   just new-bp explore                    -> bp_explore.md
#   just new-bp modify api-migration       -> bp_modify_api-migration.md
#   just new-bp python django              -> bp_python_django.md

new-bp category scenario="":
    #!/usr/bin/env bash
    set -euo pipefail

    if [ -z "{{scenario}}" ]; then
        filename="bp_{{category}}.md"
    else
        filename="bp_{{category}}_{{scenario}}.md"
    fi

    target="skills/lsp-code-analysis/references/$filename"
    template="skills/lsp-code-analysis/assets/bp_template.md"

    if [ -f "$target" ]; then
        echo "Error: $target already exists"
        exit 1
    fi

    if [ ! -f "$template" ]; then
        echo "Error: Template not found at $template"
        exit 1
    fi

    mkdir -p "skills/lsp-code-analysis/references"
    cp "$template" "$target"
    echo "Created $target"
    echo "Next steps:"
    echo "  1. Edit $target"
    echo "  2. Add entry to skills/lsp-code-analysis/SKILL.md or domain indices"

# Package a skill into a zip file
# Usage: just package <skill_name>
package skill="lsp-code-analysis":
    #!/usr/bin/env bash
    set -euo pipefail
    echo "Packaging {{skill}}..."
    mkdir -p dist
    cd skills
    zip -r ../dist/{{skill}}.zip {{skill}}/
    echo "Done! Package created at dist/{{skill}}.zip"

sync:
    uv sync --upgrade

lint path='src':
    uv run ruff check --fix {{path}}
    uv run ruff format {{path}}
    uv run ty check {{path}}

test:
    uv run pytest

check:
    uv run ruff check
    uv run ruff format --check
    uv run ty check src

# Release a new version (e.g., just release 0.1.0)
release version:
    @echo "Releasing v{{version}}..."
    # Check if version matches pyproject.toml
    @grep -q 'version = "{{version}}"' pyproject.toml || (echo "Version mismatch in pyproject.toml"; exit 1)
    # Ensure working directory is clean
    @git diff-index --quiet HEAD || (echo "Dirty working directory, please commit or stash changes"; exit 1)
    # Run tests
    uv run pytest
    # Create and push tag
    git tag v{{version}}
    git push origin main
    git push origin v{{version}}
