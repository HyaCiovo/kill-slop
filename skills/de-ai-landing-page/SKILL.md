---
name: de-ai-landing-page
description: "Create, audit, and improve websites and marketing landing pages by removing formulaic copy, weak evidence, content overload, and decorative filler. Use for page strategy, copywriting, visual design, responsive layouts, motion, and conversion reviews."
---

# De AI Landing Page

## Core goal

The first screen should quickly answer:

1. What is this, and who is it for?
2. What specific problem does it solve in which situation?
3. Where should visitors go next, and what will they get?

The rest of the page should explain why it is credible, how to start, and what costs or limits apply.

AI slop is not gradients, rounded corners, illustrations, or animation by themselves. It is decoration before information, templates before context, slogans before evidence, feature volume before user decisions, and desktop content stacked onto mobile without adaptation.

The goal is not to make every page cold or plain. Every piece of content, media, and interaction should have a clear job.

## First decision

Before auditing, improving, or building, identify the **page type and single primary conversion action**. Use these decisions to guide content, visuals, and interactions.

- **Landing page**: one audience, one core offer, one primary conversion action.
- **Homepage**: multiple audiences and secondary paths are allowed, but one primary CTA must remain clear.

If these decisions materially affect the direction and cannot be inferred from the project, ask the user and include your recommended answer.

## Modes and contextual references

Infer the mode from the request. Users do not need to memorize commands.

| Mode | Behavior | Read |
|---|---|---|
| **Audit** | Report findings, evidence gaps, priorities, and recommendations without changing files | `strategy.md`, `evidence.md`, and `review.md`, plus other files relevant to the findings |
| **Improve** | Change confirmed copy, structure, styling, and interaction issues | `strategy.md`, files for the affected scope, then `review.md` |
| **Build** | Start with audience and conversion goals, then implement and verify | All reference files in order |
| **Mobile focus** | Review density, layering, wrapping, touch behavior, and same-screen visibility | `interaction.md`, then `review.md` |

References live in this skill's `references/` directory:

| File | Contents |
|---|---|
| [strategy.md](references/strategy.md) | Audience, conversion, core message, copy, and information architecture |
| [evidence.md](references/evidence.md) | Real evidence, third-party validation, evidence gaps, and demo boundaries |
| [visual.md](references/visual.md) | Design tokens, components, motion, media, and performance |
| [interaction.md](references/interaction.md) | Mobile behavior, interaction states, accessibility, SEO, and delivery |
| [review.md](references/review.md) | Output formats and the self-review checklist |

Do not load references unrelated to the current task merely to complete a process.

## Working principles

### Decide and make clear tradeoffs

When the page, project conventions, and observed behavior provide enough evidence, act directly. Remove repeated copy, rewrite vague headings, merge sections, reorder content, redesign mobile layering, fix wrapping and overflow, and remove pointless motion or decoration.

Preserving the original is not the goal. Reorder weak structures, remove repetition, and redesign mismatched visuals instead of limiting work to sentence-level edits.

### Ask with a recommendation when direction is unclear

When choices materially change positioning, audience, brand style, or conversion paths, ask related questions together. Include:

- The observed problem.
- Your recommended option and rationale.
- Alternatives and their main tradeoffs.
- What the answer will change.

For reversible details such as font size, spacing, or local layout, follow project conventions and design principles without interrupting the user.

## Content that requires confirmation

Do not rewrite, weaken, or expand legal terms, compliance language, technical limits, safety boundaries, service scope, or contractual commitments supplied by the user without confirmation. If something appears contradictory or unclear, identify the exact passage and ask.

Keep numbers, dates, names, units, quotations, and attribution accurate. Never invent customers, features, certifications, cases, testimonials, or performance data.

Protecting facts does not mean protecting every original sentence. Ordinary marketing copy may be rewritten, merged, or removed. Ask before changing protected content.

When evidence is missing, identify the gap and recommend a resolution. Do not replace specific numbers with vague adjectives or present examples as real results.

## Rule precedence

Explicit user instructions > project conventions and brand systems > accessibility and factual accuracy > this skill's defaults.

Components, dependencies, and visual recommendations are options, not mandatory installs or a mandatory style. Reuse existing project capabilities before adding new ones.
