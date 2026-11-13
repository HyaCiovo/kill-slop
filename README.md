# Kill Slop

[中文文档](README.zh-CN.md)

A bilingual agent skill for building, auditing, and improving websites and marketing landing pages. It puts audience, context, evidence, conversion, mobile reading, and delivery quality before templates and decorative effects.

## Why this skill

- **Decisions before decoration**: identify the page type and primary conversion action before choosing visuals.
- **Evidence before claims**: use real product views, verifiable cases, third-party validation, and documented data.
- **Clear tradeoffs**: remove repetition, reorder weak structures, and redesign mismatched sections instead of making timid word edits.
- **Mobile-specific design**: layer related features and preserve manual scrolling, touch behavior, and readable typography.
- **Protected content**: never casually rewrite user-provided legal terms, technical limits, safety boundaries, or contractual commitments.
- **Real verification**: check actual desktop and mobile interactions, not only code or static screenshots.

## Languages

The English and Chinese editions are separate installable skills with the same reference structure.

| Language | Skill | Path |
|---|---|---|
| English | `kill-slop` | [`skills/kill-slop`](skills/kill-slop) |
| 中文 | `kill-slop-zh` | [`skills/kill-slop-zh`](skills/kill-slop-zh) |

Each edition contains a compact `SKILL.md` router plus five contextual references:

- `strategy.md`: audience, conversion, copy, and information architecture.
- `evidence.md`: real proof, third-party validation, and evidence gaps.
- `visual.md`: tokens, components, effects, media licensing, and performance.
- `interaction.md`: mobile behavior, accessibility, interaction states, SEO, and delivery.
- `review.md`: audit output and the agent's self-review checklist.

## Installation

Repository: [github.com/HyaCiovo/kill-slop](https://github.com/HyaCiovo/kill-slop).

### Skills CLI

```bash
npx skills add HyaCiovo/kill-slop --list
npx skills add HyaCiovo/kill-slop
```

Select `kill-slop` for English or `kill-slop-zh` for Chinese when prompted.

### Manual

Clone the repository, then copy the directory for your chosen language into the skills directory supported by your agent:

```bash
git clone https://github.com/HyaCiovo/kill-slop.git
```

See your agent's documentation for the correct skills directory. Each skill is self-contained and includes its own `references/` directory.

## Example prompts

```text
Audit this landing page. Report only conversion issues, evidence gaps, and mobile reading problems. Do not change files.
```

```text
Redesign the mobile feature section so controls and content fit together. Preserve all technical limits and factual claims.
```

```text
Build a landing page for a research data platform. Start with its audience, primary demo CTA, evidence inventory, and mobile strategy.
```

## Repository layout

```text
.
├── skills/
│   ├── kill-slop/       # English skill
│   └── kill-slop-zh/    # 中文 Skill
├── scripts/validate.py           # Dependency-free repository validation
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── CONTRIBUTING.zh-CN.md
├── README.md
├── README.zh-CN.md
└── LICENSE
```

## Development

Requires Python 3.9 or later. No third-party packages are needed.

```bash
python3 scripts/validate.py
```

The validator checks both skill editions, required references, frontmatter, relative links, and structural parity.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) or [贡献指南](CONTRIBUTING.zh-CN.md). Small, reviewable improvements are preferred. New writing-pattern rules need both a valid defect example and a protected example that should not be changed.

## Acknowledgements

The contextual review and fact-preservation ideas were partly informed by [unslop](https://github.com/theclaymethod/unslop). This repository does not include unslop's scanners, benchmarks, or codebase.

References to shadcn/ui, Base UI, ReactBits, Motion, GSAP, and Pexels are implementation and licensing guidance, not endorsements.

## License

Released under the [MIT License](LICENSE).
