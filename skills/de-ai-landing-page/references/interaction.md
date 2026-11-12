# Interaction, mobile, and delivery

## 1. Content layering and mobile

Redesign mobile reading rhythm instead of stacking desktop columns.

- Keep the core message, critical evidence, and primary CTA visible by default.
- Use tabs, swipers, or single-card presentations for related features instead of showing everything.
- Keep controls and their corresponding content on one screen when practical.
- Emphasize the current stage of a long process and move full details into secondary views.
- Horizontal labels must support free manual scrolling. Selected items may scroll into view automatically, but this must not prevent scrolling back.
- Never shrink text to an unreadable size merely to fit more content.
- Do not hide critical information in tooltips or place simple content in unnecessary modals.

Autoplay is not the default. When used, it must:

- Provide manual controls and a clear current position.
- Pause after user interaction.
- Stop outside the viewport.
- Support reduced-motion preferences.
- Avoid competing with parallax, cursor effects, or other attention-seeking motion.

## 2. Conversion and interaction states

- Use one primary CTA above the fold, with at most one secondary CTA when necessary.
- Keep the primary CTA consistent at the top and bottom. Modal titles must match the expectation set by the clicked CTA.
- Provide genuine risk reducers when available, such as a trial, phased validation, or no requirement to migrate all data first.
- Avoid dead links, empty buttons, and nonfunctional forms.
- Provide hover, active, focus, disabled, loading, and error states where applicable.
- Use persistent form labels, specific validation errors, and only necessary required fields.
- Support keyboard use and visible focus, with clear mobile menu and FAQ states.

## 3. Semantics and accessibility

- Use appropriate landmarks such as `header`, `nav`, `main`, `section`, and `footer`.
- Maintain semantic heading levels instead of using font size as a substitute.
- Meet readability and contrast requirements for text and controls.
- Give images alt text appropriate to their purpose, with empty alt text for decorative images.
- Give labels, tabs, accordions, modals, and carousels correct names, states, and keyboard behavior.
- Respect `prefers-reduced-motion`, and never let autoplay interfere with reading.

## 4. SEO and delivery

- Provide a title, description, social image, legal links, and branded favicon.
- For indexable pages, align the title and description with search intent. Use noindex for advertising or time-limited pages when appropriate.
- Consider FAQ structured data only when the content is genuine and appropriate for search; do not add it automatically.
- Check internal links, language switching, 404 pages, legal pages, and return paths from secondary pages.
- Verify form validation, submission, success, failure, and loading states rather than checking only the static interface.
