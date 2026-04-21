# Usage rules

## Clear space

Minimum clear space around the mark = the height of the mark's center node (≈ 56 px on a 512 viewBox, or ~11% of the mark's height). No typography, image, or edge may enter this zone.

## Minimum size

| Use | Min size |
|---|---|
| Favicon | 16 × 16 px |
| UI avatar | 32 × 32 px |
| Print | 0.25 inch across |

Below these sizes, use the simplified `axiom-labs-favicon.svg` variant (no ember tick, heavier center node).

## Mark vs. wordmark

| Context | Use |
|---|---|
| GitHub avatar, app icon, favicon | Mark alone (on ground) |
| Website header, README hero, slide titles | Horizontal wordmark |
| Book cover, poster, square social | Stacked wordmark |
| In running text | Never use the mark inline. Write "Axiom Labs" in the body font. |

## Axiom Labs vs. Axiom (the platform)

One mark serves both. Wordmark disambiguates:

- `[mark] AXIOM LABS` — the lab, the company, the org
- `[mark] AXIOM` — the flagship platform product (sans "LABS")

Other products in the portfolio (Dendra, Vyzier, …) get **their own distinct marks** in the same visual language (same palette, same stroke weight, different glyph). They are *not* variations of the origin glyph.

## Don'ts

- Don't rotate the mark. It has a meaningful orientation — the ember tick is the +x axis.
- Don't recolor the mark outside the palette. Graphite on off-white is the default; inverted on graphite is the alternate; monochrome versions are for printing.
- Don't place the mark on a busy photograph without a scrim.
- Don't resize the ember tick relative to the rest of the mark.
- Don't add a drop shadow, bevel, or glow. The mark is flat.
- Don't crop the mark. Use the masters provided.
- Don't reconstruct the mark from primitives in downstream tools (Keynote, PowerPoint, Word). Import the SVG or PNG; never redraw.

## Private heritage note

The burnt orange accent is a private nod to UT Austin (PMS 159). **Never** make this connection in text. Public docs, code, commits, issue threads, and paper text are kept clean of `UT`, `UTexas`, and `bbooth@` references — pre-commit hooks and CI checks enforce this. The color carries the meaning silently.
