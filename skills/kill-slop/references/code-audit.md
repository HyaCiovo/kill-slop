# Code-aware interface audit

Use source search as a map, not as proof. A regex hit, color token, component shape, or familiar phrase never proves that an interface is generic or that an edit is justified.

## 1. Scope

Confirm which app, package, route, or component set is in scope. If the repository contains multiple products with different audiences, identify the intended target instead of scanning everything indiscriminately.

Exclude dependencies, generated output, lockfiles, minified files, and version-control internals unless the user explicitly includes them. Do not read secrets or credentials.

## 2. Search the source

Use the project's available search tools to find repeated design and copy signals, including:

- Repeated gradient, glow, shadow, radius, color, and animation declarations.
- Shared card wrappers, nested panels, icon containers, badges, pills, and section labels.
- Repeated headings, vague calls to action, placeholder copy, and unsupported metrics.
- Hard-coded values that bypass existing tokens or components.
- Missing empty, loading, error, focus, disabled, and mobile states.
- Heavy dependencies or third-party scripts loaded before the primary interface.

A standalone scanner is optional. Use existing project tooling first, and never install a scanner merely to produce a larger report.

## 3. Triage in context

For every candidate, read the surrounding component, styles, content, and project conventions. Distinguish:

- **Confirmed issue**: a concrete reason shows that it harms clarity, consistency, task completion, accessibility, or performance.
- **Intentional design**: a brand token, deliberate illustration, meaningful status color, domain-specific expression, or user-requested effect.
- **Needs direction**: a choice that changes brand, audience, product behavior, or protected content and requires a recommendation-backed question.

Do not mass-edit from search results. In audit mode, report only. In improvement mode, confirmed issues may be fixed directly; ask when direction or protected behavior is at stake.

## 4. Fix at the right level

- Prefer shared tokens, base components, and content sources over repeated local patches.
- Keep diffs scoped and reviewable; do not reformat unrelated code.
- Leave other work-in-progress and unfamiliar user changes untouched.
- Preserve existing brand colors and product behavior unless a change is requested or clearly justified.
- Do not invent a new palette, metric, state, feature, or dependency to make a fix look complete.
- Remove duplication before adding another abstraction. Do not create a shared component for a one-off variation without evidence.

## 5. Verify the result

After editing, repeat targeted searches to distinguish resolved issues from intentional retained patterns. A lower hit count alone is not success.

Run the project's relevant type, lint, build, and test commands. Inspect real desktop and mobile behavior when the interface can run, including primary tasks, keyboard operation, reduced motion, loading, empty, and error states. Report retained candidates and unverified scope.
