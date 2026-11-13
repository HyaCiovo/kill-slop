# Interaction, mobile, and delivery

## 1. Content layering and mobile

Redesign mobile reading and task flow instead of stacking desktop columns.

- Keep the core message, critical evidence, primary action, and current state visible by default.
- Use tabs, swipers, or single-card presentations for related features instead of showing everything.
- Keep controls and their corresponding content on one screen when practical.
- Emphasize the current stage of a long process and move full details into secondary views.
- For data tables, preserve critical columns and move secondary detail into an expandable row or detail view; do not automatically convert every table into generic cards.
- Horizontal labels must support free manual scrolling. Selected items may scroll into view automatically, but this must not prevent scrolling back.
- Never shrink text to an unreadable size merely to fit more content.
- Do not add explanatory paragraphs by default. When a nonessential helper is genuinely useful, place it behind a semantic question-mark SVG with a tooltip that supports keyboard focus and touch.
- Do not hide critical information in tooltips or place simple content in unnecessary modals.
- Do not add refresh buttons to static or demo content without a real refresh function. Add refresh only when current data can actually be refreshed and the action provides clear user value.

Autoplay is not the default. When used, it must:

- Provide manual controls and a clear current position.
- Pause after user interaction.
- Stop outside the viewport.
- Support reduced-motion preferences.
- Avoid competing with parallax, cursor effects, or other attention-seeking motion.

## 2. Primary actions and interaction states

- Marketing pages use one primary CTA above the fold, with at most one secondary CTA when necessary. Product interfaces instead emphasize the current primary task action.
- Keep marketing CTAs consistent at the top and bottom. Modal titles must match the expectation set by the clicked action.
- Provide genuine risk reducers when available, such as a trial, phased validation, or no requirement to migrate all data first.
- Avoid dead links, empty buttons, nonfunctional forms, and actions that do not match the current object or state.
- Provide hover, active, focus, disabled, loading, empty, success, and error states where applicable.
- Empty states explain what the area is for and offer a useful next step; errors explain what failed and how to recover.
- Use persistent form labels, specific validation errors, and only necessary required fields.
- Support keyboard use and visible focus, with clear mobile menu, dialog, tabs, and accordion states.

## 3. Semantics and accessibility

- Use appropriate landmarks such as `header`, `nav`, `main`, `section`, `aside`, and `footer`.
- Maintain semantic heading levels instead of using font size as a substitute.
- Meet readability and contrast requirements for text and controls.
- Give images alt text appropriate to their purpose, with empty alt text for decorative images.
- Give labels, tabs, accordions, modals, and carousels correct names, states, and keyboard behavior.
- Respect `prefers-reduced-motion`, and never let autoplay interfere with reading or task completion.

## 4. SEO and delivery

- Public pages need a title, description, social image, legal links, and branded favicon. Do not force marketing metadata onto private product screens.
- For indexable pages, align the title and description with search intent. Use noindex for advertising, private, or time-limited pages when appropriate.
- Consider FAQ structured data only when the content is genuine and appropriate for search; do not add it automatically.
- Check internal links, language switching, 404 pages, legal pages, and return paths from secondary views.
- Verify form validation, submission, success, failure, loading, and recovery states rather than checking only the static interface.
