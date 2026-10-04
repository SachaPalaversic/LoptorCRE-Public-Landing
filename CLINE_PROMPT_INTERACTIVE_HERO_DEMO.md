# Cline Prompt — LoptorCRE Interactive Hero Demo

You are working on the public landing page for **LoptorCRE Intelligence**.

Repository: `SachaPalaversic/LoptorCRE-Public-Landing`

## Objective

Replace only the **static product preview inside the Hero** with an interactive product demonstration inspired by the clarity and polish of modern SaaS product showcases such as Kuanta.ai.

The target is the current Hero element:

```html
<section class="hero section-pad" aria-labelledby="hero-title">
  ...
  <div class="hero-product" aria-label="Product preview">
    ...
  </div>
</section>
```

The demo must feel like a real LoptorCRE workspace, not like a marketing animation or a generic carousel.

## Critical scope restriction

**Do not modify anything outside the Hero product preview unless strictly required to support this component.**

Do not change:

- The Hero headline, copy, CTA labels or CTA destinations.
- The Hero grid position or overall landing structure.
- The section `#walkthrough` and its existing six-step walkthrough.
- The six existing walkthrough steps:
  1. Bring the evidence.
  2. Keep the provenance.
  3. Surface conflicts.
  4. Choose visibility.
  5. Issue the teaser.
  6. Match anonymously.
- Pricing cards, pricing values or pricing features.
- Navigation, FAQ, footer or SEO metadata.
- Any code or deployment belonging to `app.loptorcre.com`.
- Any backend, database, authentication or real user data.

Do not move the six-step walkthrough into the Hero. The Hero demo and the six-step walkthrough are separate components.

## Existing implementation to preserve

The current landing is a static HTML/CSS/JavaScript site:

- `index.html`
- `styles.css`
- `app.js`

The existing Hero preview starts at `.hero-product` and currently contains:

- `.hero-window`
- `.app-topbar`
- `.app-layout`
- `.app-sidebar`
- `.teaser-sheet`
- `.provenance-panel`
- `.mandate-card`

Reuse this visual language and existing CSS variables. Do not introduce a new framework or dependency.

## Required interactive behaviour

Build a self-contained state machine for the Hero demo.

### Default state: Summary / institutional teaser

Keep the visual composition close to the supplied reference image:

- Dark Loptor workspace frame.
- Loptor wordmark in the top bar.
- Left navigation rail.
- Central A4 institutional teaser.
- Right-side evidence/provenance panel.
- Bottom anonymous-match mandate card.
- Verified green state and one amber Review state.

Use fictional demo data only, such as:

- Urban hotel, prime location.
- Barcelona / Spain or Valencia macro-area.
- 5,200 m² GLA, 101 keys, 4★.
- Source-controlled teaser.
- 87% anonymous fit.

### Left navigation interactions

The following left navigation items must be clickable:

1. **Summary**
   - Shows the institutional teaser and a concise asset overview.
2. **Documents**
   - Shows a document inbox with PDF, XLSX and broker-note sources.
   - One source may display `Reading` or `Review` status.
3. **Provenance**
   - Shows source-to-claim relationships.
   - A selected source highlights the related teaser datum.
4. **Matches**
   - Shows an anonymous mandate and an 87% or 92% fit indicator.
   - Identity must remain hidden.
5. **Activity**
   - Shows a small audit timeline: ingested, reviewed, teaser issued, match found.

### Right panel tabs

The right panel tabs must be clickable:

- **Provenance**
  - `asset_overview.pdf — Page 3 · Cell B12`
  - `rent_roll_2026.xlsx — Sheet 1 · Cell D8`
  - `broker_note.pdf — Page 12 · Cell C4 — Review`
- **Key data**
  - Display the main KPIs with source references.
- **Notes**
  - Display a short broker note and a visible review state.

### Evidence highlighting

When a user selects a document, source row, KPI or teaser area:

- Highlight the selected UI element with a subtle blue or green border.
- Show its source reference.
- Do not invent or silently alter the value.
- Preserve the visual hierarchy and avoid large layout shifts.

### Demo progression

Add a discreet, optional guided progression inside the Hero only. It may use:

- A small `Explore the workspace` label.
- A progress indicator or a `Next` control.
- Four to six short states.

It must not replace the existing `#walkthrough` section or duplicate its six-step content verbatim.

The user must always be able to click the interface manually. Do not force autoplay if it harms usability. If autoplay is added, pause it immediately after any manual interaction and respect `prefers-reduced-motion`.

## Design direction

Use the existing LoptorCRE visual identity:

- Background: light editorial paper tone.
- Workspace: deep navy / near-black.
- Accent: muted institutional blue.
- Verified state: restrained emerald green.
- Review state: muted amber.
- Typography: existing serif display type plus existing sans/mono UI type.
- Thin borders, restrained shadows, generous whitespace and a premium institutional feel.

The demo should look credible at desktop width and remain usable on mobile. On mobile:

- Keep the Hero copy readable.
- Make the workspace horizontally safe and responsive.
- Stack or collapse panels rather than creating inaccessible overflow.
- Ensure controls have adequate tap targets.

## Trilingual requirement

Preserve the existing EN / ES / FR language system.

All new visible UI copy must have translations in the existing `I18N` / `STATIC_UI` structures, or in a similarly simple existing structure. Do not hard-code new English-only labels into dynamically rendered states.

Verify at least:

- English: `EN`
- Spanish: `ES`
- French: `FR`

## Implementation constraints

- Vanilla HTML/CSS/JavaScript only.
- No iframe.
- No remote SaaS embed.
- No backend.
- No authentication.
- No real asset files or confidential data.
- No external tracking scripts.
- No new npm dependency unless absolutely unavoidable; prefer zero dependencies.
- Keep the existing `/manus-routes.json` intact.
- Preserve the current build command: `sh build.sh`.
- Do not alter the Vercel or Manus deployment configuration in this task.

## Acceptance criteria

Before finishing, verify:

1. The Hero still contains the original copy and both original CTAs.
2. The Hero product preview is interactive by click, not only decorative.
3. The left navigation changes the visible workspace state.
4. The right tabs change the visible evidence panel.
5. Selecting a source or KPI highlights its provenance.
6. The anonymous match keeps identity hidden.
7. The existing `#walkthrough` section is still present and still contains all six original steps.
8. Pricing content and the previously approved pricing changes remain unchanged.
9. EN, ES and FR do not produce missing labels or JavaScript errors.
10. The layout is usable on desktop and mobile.
11. `node --check app.js` passes.
12. `sh build.sh` passes.
13. `git diff --check` passes.

## Final report

Report:

- Files changed.
- Exact Hero selectors/components changed.
- How the interactive states work.
- Confirmation that `#walkthrough`, pricing and `app.loptorcre.com` were not modified.
- Validation commands and results.
