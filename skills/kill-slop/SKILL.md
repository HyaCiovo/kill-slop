---
name: kill-slop
description: "Create, audit, and improve web interfaces by removing formulaic copy, generic visuals, content overload, and decorative filler. Use for landing pages, homepages, product UI, dashboards, docs, components, responsive layouts, motion, and code-level design reviews."
---

# Kill Slop

## Scope

Use this skill for landing pages, homepages, product and pricing pages, dashboards, forms, settings, documentation, design-system components, and web prototypes. It applies to HTML/CSS, React, Vue, Svelte, Astro, other web frameworks, and interface copy.

Not every interface has a conversion CTA. Product UI has a primary user task, a current state, and a next action; documentation has a reader question and a useful answer.

## Core goal

Every interface should quickly answer:

1. What is this, and who is it for?
2. What task or problem does it address?
3. What should the user notice or do next?

Marketing pages must also establish credibility, starting costs, and limitations. Product interfaces must also expose current state, data quality, recovery paths, and operational constraints.

AI slop is not gradients, rounded corners, illustrations, or animation by themselves. It is decoration before information, templates before context, slogans before evidence, feature volume before user decisions, and desktop content stacked onto mobile without adaptation.

The goal is not to make every interface cold or plain. Every piece of content, media, and interaction should have a clear job.

## First decision

Before auditing, improving, or building, identify the **interface type and primary user task or conversion action**. Use these decisions to guide content, visuals, and interactions.

- **Landing page**: one audience, one core offer, one primary conversion action.
- **Homepage**: multiple audiences and secondary paths are allowed, but one primary CTA must remain clear.
- **Product interface**: identify the user's primary task, current state, and next action; do not invent a marketing CTA.
- **Documentation or content page**: identify the reader's question and the answer or action the page must enable.

If these decisions materially affect the direction and cannot be inferred from the project, ask the user and include your recommended answer.

## Modes and contextual references

Infer the mode from the request. Users do not need to memorize commands.

| Mode | Behavior | Read |
|---|---|---|
| **Audit** | Report findings, evidence or state gaps, priorities, and recommendations without changing files | `strategy.md`, `code-audit.md`, and `review.md`, plus other files relevant to the findings |
| **Improve** | Change confirmed copy, structure, styling, code, and interaction issues | `strategy.md`, `code-audit.md`, files for the affected scope, then `review.md` |
| **Build** | Start with audience and user goals, then implement and verify | All reference files in order |
| **Mobile focus** | Review density, layering, wrapping, touch behavior, and same-screen visibility | `interaction.md`, then `review.md` |

References live in this skill's `references/` directory:

| File | Contents |
|---|---|
| [strategy.md](references/strategy.md) | Audience, user tasks, conversion, core message, copy, and information architecture |
| [evidence.md](references/evidence.md) | Real evidence, third-party validation, evidence gaps, and demo boundaries |
| [visual.md](references/visual.md) | Design tokens, components, motion, media, and performance |
| [interaction.md](references/interaction.md) | Mobile behavior, interaction states, accessibility, SEO, and delivery |
| [code-audit.md](references/code-audit.md) | Source search, contextual triage, shared fixes, and visual regression checks |
| [review.md](references/review.md) | Output formats and the self-review checklist |

Do not load references unrelated to the current task merely to complete a process.

## Working principles

### Decide and make clear tradeoffs

When the interface, project conventions, source code, and observed behavior provide enough evidence, act directly. Remove repeated copy, rewrite vague headings, merge regions, reorder content, redesign mobile layering, fix wrapping and overflow, and remove pointless motion or decoration.

Preserving the original is not the goal. Reorder weak structures, remove repetition, and redesign mismatched visuals instead of limiting work to sentence-level edits.

When simpler works, do less. Do not add entities, controls, states, abstractions, dependencies, or explanations without a concrete user need.

### Ask with a recommendation when direction is unclear

When choices materially change positioning, audience, brand style, user tasks, or conversion paths, ask related questions together. Include:

- The observed problem.
- Your recommended option and rationale.
- Alternatives and their main tradeoffs.
- What the answer will change.

For reversible details such as font size, spacing, or local layout, follow project conventions and design principles without interrupting the user.

## Content that requires confirmation

Do not rewrite, weaken, or expand legal terms, compliance language, technical limits, safety boundaries, service scope, or contractual commitments supplied by the user without confirmation. If something appears contradictory or unclear, identify the exact passage and ask.

Keep numbers, dates, names, units, quotations, and attribution accurate. Never invent customers, features, certifications, cases, testimonials, metrics, or performance data.

Protecting facts does not mean protecting every original sentence. Ordinary interface and marketing copy may be rewritten, merged, or removed. Ask before changing protected content.

When evidence or real data is missing, identify the gap and recommend a resolution. Do not replace specific numbers with vague adjectives or present examples as real results.

## Rule precedence

Explicit user instructions > project conventions and brand systems > accessibility and factual accuracy > this skill's defaults.

Components, dependencies, scanners, and visual recommendations are options, not mandatory installs or a mandatory style. Reuse existing project capabilities before adding new ones.
