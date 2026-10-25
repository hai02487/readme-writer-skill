---
name: readme-writer
description: Write or rewrite a landing-page README for a small open-source repo. Use when a user asks for a README, a repo description, install/usage docs, or to make a repo presentable for GitHub. Works from the repo's actual code and purpose, never from invented features.
---

# readme-writer

Write a README that a stranger can understand in 30 seconds and use in 2 minutes.

## When to use this skill

Use it when the user asks to:
- Write a new README for a repo, tool, skill, or script.
- Rewrite an existing README that is empty, vague, or out of date.
- Make a repo ready to publish on GitHub.

## When NOT to use it

- Do not use it to document a repo you have not inspected. Read the code first.
- Do not use it for a full website, a tutorial series, or API reference docs.
  Those are separate jobs; this skill writes one README only.
- Do not use it to invent a feature, a command, or a result the code does not have.

## Workflow

### 1. Inspect before writing
Read, in this order:
1. The entry point and the main command or function.
2. The install path (package file, script, or setup steps).
3. Any existing README, examples, and tests.
4. The licence file, if one exists.

Write down, in your own notes: what the project does, who it is for, how it is
installed, and one command that actually works. If any of those four is unknown,
find it in the code or ask the user — never guess it.

### 2. Draft in this fixed order
1. One-line description: what it does, for whom, and the main benefit.
2. What it does and what it does NOT do (scope honesty, two short lists).
3. Install: one command that works on a clean machine.
4. Usage: the main command, with real output.
5. Examples: at least two — the main job, and one edge case or common mistake.
6. How it is tested: the exact test command.
7. Contributing and licence.

### 3. Verify every command and claim
- Run the install and usage commands yourself, or state clearly that you have
  not run them and the user must check them. Never present an untested command
  as if it were tested.
- Check every feature you mention exists in the code. Delete anything you
  cannot point to in a file.
- Check for placeholder text (unfinished markers, promised-but-missing
  features, filler text). Any hit blocks delivery until it is replaced with
  real content or removed.

### 4. Keep it tight
- First screen (before scrolling) must answer: what, who, install, one example.
- No marketing fluff, no superlatives the project has not earned, no fake
  badges for tests or coverage that do not exist.
- Badges only for things that are true and verifiable (for example, a CI badge
  only when CI is actually configured).

## Good example (one-line description)

> A Python CLI that converts CSV and JSON files into GitHub-Flavoured Markdown
> tables, offline, with no dependencies.

It names the job, the audience is implied by the tool type, and it states two
verifiable facts: offline, no dependencies.

## Bad example (do not write like this)

> The best, fastest, most powerful README generator in the world, with AI
> superpowers and unlimited features promised for later!

It claims "best" and "fastest" with no evidence, promises features that do not
exist, and tells the reader nothing about what the tool actually does.

## Output rules

- Output the complete README, ready to save as `README.md`.
- If the repo has no licence, say so plainly and suggest adding one — do not
  claim a licence it does not have.
- If a requested feature is missing from the code, list it under
  "Not yet implemented" or leave it out — never describe it as working.
- End with a short checklist of what you verified (commands run, files read)
  and anything the user still needs to check.
