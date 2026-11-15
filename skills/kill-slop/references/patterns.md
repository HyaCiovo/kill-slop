# Slop patterns and remediation

Use this catalogue to recognize common machine-default decisions and choose a concrete fix. These are contextual candidates, not a lint ruleset. A deliberate brand choice, meaningful status, real sequence, or user-requested effect can be valid.

Record findings as `pattern ID + file:line + observed problem + proposed fix`. Never mass-edit from pattern matching alone.

## 1. Color and surfaces

| ID | Pattern | Remediation |
|---|---|---|
| C01 | Default indigo-to-violet gradients on buttons, heroes, and cards | Use one justified brand accent and a flat surface. Remove colored glow shadows unless they point to a specific element. |
| C02 | Gradient-clipped headlines or multiple highlighted keywords | Use solid text and establish emphasis through size, weight, position, and sentence structure. Keep at most one meaningful accent. |
| C03 | Atmospheric page gradients, tinted card washes, and colored glow used to appear premium | Hold one flat background. Separate surfaces with a hairline or restrained neutral shadow, not decorative color washes. |
| C04 | Stock semantic rainbow or a status box with border, text, and background all in one hue | Carry state in words and weight first. Use a neutral surface with one intentional semantic accent from the project palette. |

## 2. Typography and emphasis

| ID | Pattern | Remediation |
|---|---|---|
| T01 | Serif-italic emphasis on one word, decorative strikes, underlines, or highlighter swipes | Use weight, position, or a meaningful line break. Keep strike for edits, underline for links, and highlighting for real annotation. |
| T02 | A tracked uppercase kicker above every heading that merely restates the heading | Delete redundant labels. Keep a kicker only when it adds a category, date, status, or genuine sequence. |
| T03 | A full marketing sentence at display size, wrapping into three or four lines and consuming the first viewport | Put the core point into a short heading and move mechanism or detail into normal-size supporting copy. Recheck line breaks at real widths. |
| T04 | Flat type hierarchy, or terminal/editorial typography applied to a product regardless of its task | Create a small scale with meaningful steps. Match type to the job: legible UI sans and tabular numerals for scanning, editorial serif only for genuinely editorial content, monospace for code. |

## 3. Copy and evidence

| ID | Pattern | Remediation |
|---|---|---|
| W01 | "Not just X, it's Y", slogan fragments, jargon, dramatic triads, and vague transformation claims | Say who does what, in which situation, with what concrete mechanism or outcome. Remove any framing that adds no information. |
| W02 | Invented stat rows, fake logo walls, anonymous testimonials, fake dashboards, or sample data presented as real results | Remove unsupported proof. Use a real product view, a traceable case, or a documented number. Label a demo once when confusion is possible, without repeated mock disclaimers. |

## 4. Components and containers

| ID | Pattern | Remediation |
|---|---|---|
| U01 | Emoji everywhere, text characters used as icons, crude placeholder SVG marks, or an icon tile on every feature | Use semantic SVG icons from the project library or deliberate inline SVG. Remove icons that add no meaning; never use emoji or text glyphs as interface decoration. |
| U02 | Pulsing glowing status dots, decorative New/Popular/Beta pills, and thick rings used to manufacture importance | Use a small flat dot plus a word only for real state. Keep badges for real status or version. Remove decorative emphasis. |
| U03 | Maximum-radius glass panes, oversized diffuse shadows, tinted glow, or border plus heavy shadow doing the same separation job | Use a consistent radius scale and solid surfaces. Choose a hairline or a restrained neutral elevation shadow, not both without reason. |
| U04 | Nested corners that do not nest, or borders disappearing at rounded corners because radius and stroke sit on different boxes | Compute inner radius from outer radius minus the gap, or keep the inner element square. Put border and radius on the same box; keep true dividers straight. |
| U05 | Cards inside cards, repeated callouts with colored left borders, and equal-weight all-caps card grids | Use one surface per region. Group with spacing, alignment, and hairlines; keep callouts for genuine asides and show the most important content fully. |
| U06 | Ornamental 01/02/03 markers on sections, navigation items, checklists, feature lists, or any unordered content, including a numbered index that only mirrors the navigation | Number only genuine user-facing sequences such as ordered steps, rankings, or versions. Remove section numbers, navigation numbers, and decorative index numerals even when they look like a table of contents; drop the same markers from checklists, benefits, and feature lists. |
| U07 | Decorative micro-eyebrows: tiny tracked or caps labels above every heading, section names repeated as small kickers, status lines or English sub-labels added for texture | Delete labels that only restate the heading or the navigation. Keep a kicker only when it carries a real category, date, status, or sequence, and let the heading name the section. At most one informative eyebrow per region; apply the same rule to micro-labels inside cards. |
| U08 | Rule-carpet layout: hairlines on every section, row, list item, card field, and nav item, so borders substitute for spacing | Remove rules that only decorate. Keep at most one rule per group (table header, document edge, sticky bar) and group with proximity, alignment, and whitespace instead. Never stack a section rule, a row rule, and a card border around the same content. |
| U09 | Spacing without optical rhythm: arbitrary margins, identical gaps for related and unrelated content, cramped CJK leading, and sections floating inside oversized empty bands | Use one spacing scale and apply it by relationship: related items close, separate groups apart. Match leading to the script (CJK body roughly 1.7-1.9, display 1.1-1.25), check the result at real widths and on mobile, and delete empty bands that do not separate meaning. |
| U10 | Diffuse shadow used as fake elevation: a small card or icon with a large low-opacity blur, little or no offset, or a colored shadow or glow | Remove the shadow by default and use spacing or a hairline. If elevation is real, use a small neutral shadow with a short blur, slight offset, and low opacity. Do not combine a heavy shadow with a competing border, and inspect the rendered result. |

## 5. Motion

| ID | Pattern | Remediation |
|---|---|---|
| M01 | Scale/bounce/lift on every hover and `transition-all` by default | Transition only properties that communicate state. Prefer a subtle surface or color shift; reserve springs for elements that genuinely move through space. |
| M02 | Wobbling off-center spinners, autoplay combined with parallax or cursor effects, and scroll reveals on every region | Center spinner artwork and rotate around a fixed point. Remove competing effects, stop autoplay after interaction and outside the viewport, and provide reduced-motion behavior. |

## 6. Layout and interaction

| ID | Pattern | Remediation |
|---|---|---|
| L01 | Desktop grids stacked directly onto mobile, controls separated from their content, or all features expanded into a long feed | Recompose mobile reading and task flow. Use tabs or a single active view, preserve manual scrolling, and keep controls with corresponding content when practical. |
| L02 | Unnecessary refresh buttons, explanatory paragraphs, helper copy on every block, or repeated mock/simulated warnings | Remove controls without real function. Put nonessential helper content behind an accessible question-mark SVG tooltip; keep critical information visible and label demo provenance at most once. |

## Remediation order

1. Confirm the primary user task and intended brand direction.
2. Fix shared tokens and theme decisions.
3. Fix base components and shared content sources.
4. Address one-off layout, style, and copy issues.
5. Re-run targeted searches and inspect real desktop and mobile behavior.

A lower pattern count is not proof of a better interface. Verify clarity, task completion, accessibility, performance, and factual accuracy.
