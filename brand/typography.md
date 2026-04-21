# Typography

## Primary — Space Grotesk

Used for wordmarks, product marks, UI headings, figure titles, and anything with a display or branded role.

- Download: [Space Grotesk on Google Fonts](https://fonts.google.com/specimen/Space+Grotesk)
- License: SIL Open Font License 1.1 — bundle with any distribution
- Weights in use: 400 (Regular), 500 (Medium), 700 (Bold)
- Wordmark setting: Medium, all caps, tracked to 180/1000 (`letter-spacing: 0.18em`)

## Secondary — system stack for body text

Avoid serving a second display font. Body copy inherits from the OS stack so pages stay light and familiar.

```css
font-family:
  -apple-system,
  "SF Pro Text",
  system-ui,
  "Segoe UI",
  Roboto,
  "Helvetica Neue",
  Arial,
  sans-serif;
```

## Monospace — for code, numbers, diagnostic output

JetBrains Mono or the system monospace. Weight 400.

```css
font-family: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
```

## Type scale

Base 16 px. Ratio 1.25 (major third).

| Role | Size | Line-height | Weight |
|---|---|---|---|
| Display | 64 | 1.05 | 500 |
| H1 | 48 | 1.1 | 500 |
| H2 | 32 | 1.2 | 500 |
| H3 | 24 | 1.3 | 500 |
| H4 | 20 | 1.35 | 500 |
| Body | 16 | 1.55 | 400 |
| Caption | 13 | 1.45 | 400 |
| Micro / label | 11 | 1.4 | 500, tracked 0.05em |

## Paper / LaTeX

See `templates/axiom-labs-preamble.tex`. Papers use a serif face for body (TeX Gyre Pagella) and Space Grotesk for figure labels and titles. The justification: academic convention expects a serif body; branded display still reads on figures and covers.

## Usage rules

- **Never** stretch, slant, or outline the wordmark typography. If you need a different weight, use it; don't manufacture one.
- **Never** reset wordmark tracking. `0.18em` caps-tracking is what makes "AXIOM LABS" look like the wordmark and not just the words.
- **Do** outline text in production SVG exports (Inkscape: Path → Object to Path). Rendering-device font substitution is the #1 cause of wordmark drift.
