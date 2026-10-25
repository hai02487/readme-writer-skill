"""Validation tests for the readme-writer skill file.

Run: python3 tests/test_skill.py
No third-party dependencies are needed.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "readme-writer" / "SKILL.md"
README = ROOT / "README.md"


def test_skill_frontmatter():
    text = SKILL.read_text(encoding="utf-8")
    assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
    frontmatter = text.split("---", 2)[1]
    assert re.search(r"^name:\s*readme-writer\s*$", frontmatter, re.M) is not None
    assert re.search(r"^description:\s*.+", frontmatter, re.M) is not None


def test_skill_sections():
    text = SKILL.read_text(encoding="utf-8")
    for heading in ("When to use this skill", "When NOT to use it",
                    "Workflow", "Output rules"):
        assert heading in text, f"missing section: {heading}"


def test_no_placeholders():
    banned = ("TODO", "coming soon", "lorem")
    for path in (SKILL, README):
        # Drop the one instruction line that *lists* banned phrases, so the
        # check catches real placeholders instead of its own explanation.
        lines = [line for line in path.read_text(encoding="utf-8").splitlines()
                 if "placeholder text:" not in line.lower()]
        lower = "\n".join(lines).lower()
        for word in banned:
            assert word not in lower, f"{path.name} contains placeholder: {word}"


def test_readme_sections():
    text = README.read_text(encoding="utf-8")
    for heading in ("What it does", "What it does NOT do", "Install",
                    "Usage", "Example", "How it is tested", "Licence"):
        assert heading in text, f"README missing section: {heading}"


def main():
    tests = [test_skill_frontmatter, test_skill_sections,
             test_no_placeholders, test_readme_sections]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"All {len(tests)} tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
