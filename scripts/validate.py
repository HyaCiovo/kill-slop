#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("de-ai-landing-page", "de-ai-landing-page-zh")
REFERENCES = (
    "strategy.md",
    "evidence.md",
    "visual.md",
    "interaction.md",
    "review.md",
)
REQUIRED_FILES = (
    "README.md",
    "README.zh-CN.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING.zh-CN.md",
    "LICENSE",
)

errors: list[str] = []


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(path, "missing YAML frontmatter")
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(path, f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def heading_outline(path: Path) -> list[int]:
    return [
        len(match.group(1))
        for line in path.read_text(encoding="utf-8").splitlines()
        if (match := re.match(r"^(#{1,6})\s+", line))
    ]


for relative in REQUIRED_FILES:
    if not (ROOT / relative).is_file():
        errors.append(f"Missing required file: {relative}")

outlines: dict[str, dict[str, list[int]]] = {}
for skill_name in SKILLS:
    skill_dir = ROOT / "skills" / skill_name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"Missing skill: {skill_name}/SKILL.md")
        continue

    metadata = frontmatter(skill_file)
    if metadata.get("name") != skill_name:
        fail(skill_file, f"name must be {skill_name}")
    if not metadata.get("description"):
        fail(skill_file, "description is required")

    outlines[skill_name] = {"SKILL.md": heading_outline(skill_file)}
    for reference in REFERENCES:
        path = skill_dir / "references" / reference
        if not path.is_file():
            errors.append(f"Missing reference: {skill_name}/references/{reference}")
        else:
            outlines[skill_name][reference] = heading_outline(path)

if len(outlines) == len(SKILLS):
    english = outlines[SKILLS[0]]
    chinese = outlines[SKILLS[1]]
    for name in english:
        if name not in chinese:
            continue
        if english[name] != chinese[name]:
            errors.append(f"Heading structure differs between language editions: {name}")

markdown_files = [ROOT / name for name in REQUIRED_FILES if name.endswith(".md")]
for skill_name in SKILLS:
    skill_dir = ROOT / "skills" / skill_name
    markdown_files.append(skill_dir / "SKILL.md")
    markdown_files.extend(skill_dir / "references" / name for name in REFERENCES)

link_pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
checked_links = 0
for path in markdown_files:
    if not path.is_file():
        continue
    for target in link_pattern.findall(path.read_text(encoding="utf-8")):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        checked_links += 1
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(ROOT):
            fail(path, f"link points outside the repository: {target}")
        elif not resolved.exists():
            fail(path, f"broken relative link: {target}")

if errors:
    print("Validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"Validated {len(SKILLS)} skill editions, {len(REFERENCES)} references each, and {checked_links} relative links.")
