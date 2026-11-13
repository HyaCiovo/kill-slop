# Kill Slop

[中文文档](README.zh-CN.md)

A bilingual agent skill for building, auditing, and improving web interfaces: landing pages, homepages, dashboards, product UI, documentation, forms, components, and prototypes. It puts user tasks, context, evidence, mobile reading, accessibility, and delivery quality before templates and decorative effects.

## Why this skill

- **Decisions before decoration**: identify the interface type and primary user task or conversion action before choosing visuals.
- **Evidence before claims**: use real product views, verifiable cases, third-party validation, and documented data.
- **Clear tradeoffs**: remove repetition, reorder weak structures, and redesign mismatched regions instead of making timid word edits.
- **Code-aware review**: search source for repeated patterns, confirm them in context, and prefer shared token or component fixes.
- **Mobile-specific design**: layer related features and preserve manual scrolling, touch behavior, and readable typography.
- **Protected content**: never casually rewrite user-provided legal terms, technical limits, safety boundaries, or contractual commitments.
- **Real verification**: check actual desktop and mobile interactions, not only code or static screenshots.

## Languages

The English and Chinese editions are separate installable skills with the same reference structure.

| Language | Skill | Path |
|---|---|---|
| English | `kill-slop` | [`skills/kill-slop`](skills/kill-slop) |
| 中文 | `kill-slop-zh` | [`skills/kill-slop-zh`](skills/kill-slop-zh) |

Each edition contains a compact `SKILL.md` router plus six contextual references:

- `strategy.md`: audience, user tasks, conversion, copy, and information architecture.
- `evidence.md`: real proof, third-party validation, and evidence gaps.
- `visual.md`: tokens, components, effects, media licensing, and performance.
- `interaction.md`: mobile behavior, accessibility, interaction states, SEO, and delivery.
- `code-audit.md`: source search, contextual triage, shared fixes, and visual checks.
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
Audit this web project for generic visual patterns and unclear interface copy. Do not change files.
```

```text
Review this dashboard's empty, loading, error, and mobile states. Preserve all technical constraints.
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
│   ├── kill-slop/                # English skill
│   └── kill-slop-zh/             # 中文 Skill
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

The contextual review and fact-preservation ideas were partly informed by [unslop](https://github.com/theclaymethod/unslop). Source-level triage and remediation guidance were informed by [kill-ai-slop](https://github.com/yetone/kill-ai-slop). This repository does not include their scanners, benchmarks, or codebases.

References to shadcn/ui, Base UI, ReactBits, Motion, GSAP, and Pexels are implementation and licensing guidance, not endorsements.

## License

Released under the [MIT License](LICENSE).
