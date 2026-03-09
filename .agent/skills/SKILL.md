---
name: Example Skill
description: Template for creating a new custom agent skill.
---

# Skill Template

Use this file as a starting point when creating a new skill in `.agent/skills/`.

## Structure

A skill lives in its own folder under `.agent/skills/`:

```
.agent/skills/my-skill/
├── SKILL.md       # Instructions for the agent (this file)
├── scripts/       # Optional helper scripts
└── templates/     # Optional code or file templates
```

## Writing a Skill

1. **Frontmatter** — set `name` and `description` at the top of `SKILL.md`
2. **Instructions** — write clear, step-by-step markdown that the agent follows
3. **Context** — include any constraints, edge cases, or rules specific to this skill
4. **Examples** — add before/after examples or sample outputs where helpful

## Example

```markdown
---
name: Add Endpoint
description: Adds a new REST endpoint to the Python API following project conventions.
---

## Steps

1. Create a route handler in `src/aigravscode/routes/`
2. Register the route in `main.py`
3. Add a test in `tests/` that covers the happy path and one error case
4. Update the API docs in `docs/`
```
