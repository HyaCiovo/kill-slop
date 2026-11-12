# Contributing

[中文贡献指南](CONTRIBUTING.zh-CN.md)

Thank you for improving De AI Landing Page. Keep changes focused, reviewable, and grounded in real page outcomes.

## Ways to contribute

- Improve page strategy, evidence, mobile behavior, accessibility, or delivery guidance.
- Add examples of formulaic page patterns and the conditions under which they actually cause harm.
- Improve either language edition or fix translation drift.
- Improve repository validation and documentation.

## Design-rule contributions

Do not add universal bans based only on personal taste. A new writing or design pattern should include:

1. A confirmed example showing the problem in context.
2. A protected example where the same pattern is valid and should remain unchanged.
3. The reasoning and intended outcome.
4. Any legal, technical, accessibility, or factual constraints.

Do not contribute invented customer claims, fabricated performance results, or copied proprietary content.

## Translation parity

Keep the English and Chinese reference structures aligned. When changing one edition, update the other or clearly explain why the difference is intentional.

## Local validation

```bash
python3 scripts/validate.py
```

Validation must pass before opening a pull request. For documentation-only changes, no application build is required.

## Pull requests

- Keep one logical change per pull request.
- Describe the user-facing or agent-facing improvement.
- Link relevant issues and examples.
- List what you verified and anything left unverified.

Be respectful and constructive. Assume good faith, discuss evidence, and keep feedback focused on the work.
