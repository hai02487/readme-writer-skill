# readme-writer-skill

An agent skill that writes a landing-page README for a small open-source repo — from the repo's actual code and purpose, never from invented features.

## What it does

When an AI coding agent loads this skill, it:
- Inspects the repo's entry point, install path, examples, and tests before writing.
- Writes a README in a fixed order: one-line description, scope, install, usage with real output, examples, testing, contributing, licence.
- Verifies every command and claim it writes, and refuses vague, untested, or invented content.

## What it does NOT do

- It does not write a full website, tutorial series, or API reference.
- It does not document a repo it has not inspected.
- It does not invent features, commands, or results.

## Who it is for

Developers publishing a small tool, CLI, or skill on GitHub who want a README a stranger can understand in 30 seconds and use in 2 minutes.

## Install

This skill follows the open Agent Skills format: a folder with a `SKILL.md` file.

**Claude Code / Codex / Gemini CLI (project level):**

```bash
mkdir -p .agents/skills
cp -r skills/readme-writer .agents/skills/readme-writer
```

**User level (available in all projects):**

```bash
mkdir -p ~/.agents/skills
cp -r skills/readme-writer ~/.agents/skills/readme-writer
```

Then ask your agent, for example: "Write a README for this repo using the readme-writer skill."

## Usage

With the skill installed, a typical request is:

> Write a README for this repo using the readme-writer skill.

The agent will inspect the code first, then return a complete `README.md` in the order above, plus a short checklist of what it verified and anything you still need to check.

## Example

For a small CSV-to-Markdown CLI, the skill produces a first screen like this:

> A Python CLI that converts CSV and JSON files into GitHub-Flavoured Markdown tables, offline, with no dependencies.
>
> Install: `pip install markdown-table-converter` (example — replace with the real install for your project)
>
> Usage: `csv-to-md data.csv`

The real skill output always uses the actual install command and usage from the repo being documented — the lines above are only an illustration of the shape, not a claim about this repo.

## How it is tested

The skill file is validated, not executed, so the test gate is:

```bash
python3 tests/test_skill.py
```

That script checks that `SKILL.md` has valid `name` and `description` frontmatter, the required workflow sections (When to use, When NOT to use, Workflow, Output rules), and no unfinished placeholder content.

## Structure

```
readme-writer-skill/
  skills/readme-writer/SKILL.md   The skill itself
  tests/test_skill.py             Validation tests for the skill file
  examples/                       A short before/after README example
  README.md
  LICENSE
  CONTRIBUTING.md
  SECURITY.md
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Small, focused improvements are welcome: a clearer example, a tighter workflow step, or a new edge case the skill should handle.

## Licence

MIT — see [LICENSE](LICENSE).
