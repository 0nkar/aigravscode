---
name: Example Skill
description: A template for creating a new custom skill for the Antigravity agent.
---

# Example Skill Instructions

This is a template for creating a new skill. Skills allow you to teach the agent complex or specific tasks by providing detailed instructions and resources.

## Structure

A skill folder (e.g., `.agent/skills/my-skill/`) should contain:
- `SKILL.md`: The main instruction file (this file).
- `scripts/`: (Optional) Helper scripts or utilities.
- `templates/`: (Optional) Code templates.

## How to Write a Skill

1. **Frontmatter**: Define the `name` and `description` in the YAML frontmatter at the top of the file.
2. **Instructions**: Write clear, step-by-step instructions in Markdown.
3. **Context**: Provide any necessary context or rules the agent should follow when using this skill.
