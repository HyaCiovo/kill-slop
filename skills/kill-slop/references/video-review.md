# Optional comparison and story videos

Use video only when recorded evidence or a shareable transformation is genuinely useful. Choose one of two modes:

- **Comparison video**: record the same real interaction before and after a change.
- **Story video**: a square, roughly ten-second presentation in which one screen transforms through several visible design passes.

For static copy, spacing, or color changes, use screenshots instead. Do not install Playwright, browsers, or FFmpeg unless the user requests a recording or the task clearly needs one.

## 1. Prepare the tools

Reuse project dependencies and installed tools first. If recording is requested and tools are missing, explain what will be installed and why:

```bash
# Use the project's package manager when adding the development dependency.
npm install --save-dev playwright
npx playwright install chromium

# Check video encoding availability.
ffmpeg -version
```

If FFmpeg is missing, use the operating system's normal package manager, such as `brew install ffmpeg` on macOS, after confirming the installation with the user. Do not use sudo or modify production dependencies for a review-only task.

Keep outputs under `artifacts/` and do not commit them unless the user explicitly wants published examples. Never expose credentials, private customer data, or personal information.

## 2. Record a fair comparison

Use the same route, locale, viewport, device scale, data, initial state, and action sequence before and after the change. Wait for fonts, images, and the relevant state. Use reduced motion for static comparisons; when motion is being reviewed, keep motion settings identical.

Create a temporary Playwright script suited to the project:

```ts
import { chromium } from "playwright";

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  recordVideo: {
    dir: "artifacts/design-comparison/raw",
    size: { width: 1440, height: 900 },
  },
});
const page = await context.newPage();
await page.goto("http://127.0.0.1:3000", { waitUntil: "networkidle" });
await page.evaluate(() => document.fonts.ready);
// Perform the scenario with real role-based locators.
await context.close();
await browser.close();
```

Run the same scenario for `before.webm` and `after.webm`. For mobile, use actual touch and mobile context options rather than only narrowing a desktop viewport.

## 3. Combine a comparison with FFmpeg

When both recordings use the same dimensions, place before on the left and after on the right:

```bash
ffmpeg \
  -i artifacts/design-comparison/before.webm \
  -i artifacts/design-comparison/after.webm \
  -filter_complex "[0:v]fps=30,scale=1440:900,setsar=1[a];[1:v]fps=30,scale=1440:900,setsar=1[b];[a][b]hstack=inputs=2[v]" \
  -map "[v]" -c:v libx264 -pix_fmt yuv420p -movflags +faststart \
  artifacts/design-comparison/comparison.mp4
```

Change the scale to the actual recording dimensions. Do not upscale low-quality recordings merely to make them larger.

## 4. Build a story video

The story video method is adapted from Damir Sokolovsky's [unslop](https://github.com/heydamir/unslop), licensed CC BY 4.0. Keep the small `unslop by @heydamir` credit on videos made with this workflow and preserve the attribution in `NOTICE`.

### Story structure

- Use a standalone `artifacts/story/story.html` containing the original screen and its styles. Do not change the production page for presentation purposes.
- Use three to five visible steps, such as spacing, color and icons, type and copy, then details. List them in `<meta name="kill-slop-steps" content="Spacing, Color and icons, Type and copy, Details">`.
- Add step classes cumulatively: `.s1`, `.s2`, `.s3`, and so on. Each step only changes presentation values on the same DOM, allowing the old state to morph into the new one.
- Stagger changes slightly from the top left across the screen, creating a wave rather than a full-screen cut.
- Keep the screen and its own background as the only visual frame. Do not add an outer window, card, border, or shadow.
- Render square and close on the area with the most visible change, with a total duration of about ten seconds or less.

### Morphing rules

- Change padding, gaps, sizes, colors, radii, and shadows in place. Avoid replacing the page or rebuilding the DOM.
- Fade gradients, glows, and washes on separate layers while the underlying solid color changes.
- Use explicit pixel radii instead of `9999px` when a pill shape must morph.
- Roll or blur only text that actually changes, with at most eight text swaps in one story. Size, weight, tracking, and color changes should tween without swaps.
- Crossfade replacement icons in the same box. Collapse removed decorative items and fade in new meaningful items while reserving space to prevent layout jumps.
- Keep the story page at a fixed presentation size rather than depending on `100vh`.

### Redlines and camera

- Start with a short redline beat on the clearest slop examples, using no more than five short tags.
- Show live spacing measurements on four to six meaningful gaps, not every row. Measurements follow the elements and update from the old value to the new one.
- Outline two to four changing corners and show their radius values.
- Define the crop in page coordinates with `<meta name="kill-slop-frame" content="0 0 960">`, using x, y, and width. Point at the screen's top left and keep the crop tight enough for phone viewing.
- If a window grows wider, anchor it to the left so it expands to the right rather than drifting sideways.

### Record the story

Use Playwright to load the story file and apply step classes in order, with time for each transition to finish. Record the result as WebM, then use FFmpeg to crop or scale the square output and encode MP4 with H.264, `yuv420p`, and fast-start playback. Do not fetch or execute an unreviewed remote renderer.

The story file is a presentation artifact. The clean result still ships in the project's normal stack without story classes, measurement tags, or presentation attributes.

## 5. Verify and deliver

- Play the resulting video and inspect the beginning, every major step, and the end.
- For comparisons, confirm that both sides show the same real task and intended difference.
- For stories, confirm that changes morph in place, redlines remain attached, text is readable, and the full sequence fits the intended duration.
- Check that controls are not cropped and no private information appears.
- Extract a few frames with FFmpeg when a detailed visual check is needed.
- Report the local video path, route, viewport or crop, scenario, and anything not captured.
- Remove temporary scripts and intermediate recordings when they are no longer needed.
- Do not upload or publish recordings without an explicit request.

A comparison video is evidence only when it records real behavior. A story video is a presentation of the design transformation, not proof of functionality by itself.
