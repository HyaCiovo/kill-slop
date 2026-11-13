# Visual design, motion, and media

## 1. Visual system

Use existing project tokens, fonts, and brand conventions first. This skill must not override a mature design system. Define typography, line height, spacing, radii, borders, and colors only when no design system exists.

Defaults:

- Use no more than two typefaces, with clear weights and hierarchy.
- Avoid orphaned words in headings and allow body copy to wrap naturally.
- Keep muted text readable and meet WCAG AA for body copy.
- Keep card nesting to two levels by default.
- Use shared tokens for radii, spacing, line height, and page margins.
- Use primary colors with restraint. Gradients, glow, and glass effects need a clear purpose.
- Do not repeat "large heading, gray subtitle, three cards" across every section.
- Do not use abstract spheres, fake 3D, default icon discs, or abstract UI mockups to fill space.
- Do not use emoji in interface copy, status markers, navigation, or decoration.
- Use semantic SVG icons from the project's icon library or deliberate inline SVG. Do not imitate icons with text characters or add an icon merely to fill space.
- Keep meaningless decorative symbols out of the copy.
- Do not add sections, cards, controls, labels, helper text, or decorative assets without a distinct user need.

There is no single approved visual style. Editorial, industrial, playful, or minimal directions can all work when they match the audience, evidence, and brand.

## 2. Components and effects

Reuse project components and dependencies first. Confirm the framework, versions, package manager, and interaction system. Do not add a dependency when CSS or an existing library can reasonably do the job.

When new capabilities are justified:

- **Base components**: when adopting shadcn/ui, prefer its Base UI version while preserving project tokens, keyboard behavior, and focus states. Do not ship the default skin unchanged.
- **Expressive effects**: ReactBits can be installed for particles, text decomposition, and special hover effects when they strengthen the hero, primary CTA, or brand recall. For non-React projects, choose a Bits version or equivalent implementation built for that framework.
- **Gestures and state motion**: consider Motion in React projects for gestures, layout changes, and local transitions.
- **Parallax and complex scenes**: consider GSAP for scroll timelines and complex choreography, or Motion when it fits the existing React stack. Do not install a large animation library for a simple fade or translate.

Before installing, explain what the dependency enables that the existing approach cannot reasonably provide. After implementation, check bundle size, mobile performance, touch behavior, and reduced-motion support. Do not copy an effect solely because its demo looks impressive.

## 3. Motion and decoration

Motion should support attention, state feedback, and spatial relationships. Keep the page quiet by default. Do not require scroll reveals for every section or a word-by-word tagline reveal.

A page may contain a small number of brand moments, but there is no quota. Before adding one, ask:

- Does it strengthen the core message or a key action?
- Does it harm reading, performance, or accessibility?
- Can it degrade gracefully?
- Does it compete with neighboring sections?

Prefer animating transform and opacity, and respect `prefers-reduced-motion`.

## 4. Images and licensing

For decorative imagery, prefer libraries that allow free commercial use. Pexels is the recommended default. Record the source and check the current license for each image and intended use. Compress and lazy-load images and provide appropriate alt text.

If the user has purchased ReactBits Pro, a paid media library, or other assets, those resources may be used when the license covers the intended use. Do not force a free replacement. Never assume a purchase or license coverage.

Stock imagery supports reading rhythm only. Decorative assets must not impersonate product evidence. Real product screenshots and real use-case evidence remain preferable to generic media.

## 5. First-screen and resource performance

Visual effects must not make the first screen unusable:

- Prioritize the core message, primary CTA, and critical hero media. Defer secondary demos, carousels, and third-party scripts.
- Do not let analytics, chat, ads, or other third-party scripts block first-screen rendering or interaction.
- Load only required font character sets, weights, and styles. Preload critical fonts selectively and set an appropriate `font-display`; never preload every font.
- Give hero images explicit dimensions to prevent layout shifts, and lazy-load offscreen images.
- Split or defer complex animation, Three.js, GSAP scenes, and large components by route or viewport.
- Follow existing project performance budgets. Without a budget, inspect Core Web Vitals, first-screen requests, and mobile interaction responsiveness.
