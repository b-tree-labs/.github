# Palette

| Role | Name | Hex | Notes |
|---|---|---|---|
| Primary ink | Graphite | `#1a1a1f` | Body text, primary mark strokes, wordmark |
| Primary ground | Warm off-white | `#f8f6f1` | Page background, card ground |
| Accent | Burnt orange | `#BF5700` | The +x tick on the mark, any single accent element. PMS 159. Use sparingly — never more than one accent per composition. |

## Extended palette (derived)

Only when the primary three are insufficient. Don't invent new accents.

| Role | Name | Hex | Notes |
|---|---|---|---|
| Soft ink | Graphite 70 | `#6a6a72` | Captions, meta-text |
| Soft ground | Sand | `#efece6` | Page chrome, borders-as-surfaces |
| Rule line | Dust | `#d8d3c9` | Hairlines, dividers |
| Accent — deep | Ember deep | `#8a3d00` | Hover/pressed states for `#BF5700` |
| Accent — soft | Ember wash | `#f4e4d8` | Background tints beneath accent elements |

## Semantic tokens

Use these in CSS / matplotlib / LaTeX — not raw hex.

```css
:root {
  --ink: #1a1a1f;
  --ground: #f8f6f1;
  --accent: #BF5700;
  --ink-soft: #6a6a72;
  --ground-soft: #efece6;
  --rule: #d8d3c9;
  --accent-deep: #8a3d00;
  --accent-wash: #f4e4d8;
}
```

## Contrast

| Foreground | Background | Ratio | WCAG |
|---|---|---|---|
| `#1a1a1f` | `#f8f6f1` | 15.3 : 1 | AAA (everything) |
| `#1a1a1f` | `#efece6` | 13.1 : 1 | AAA |
| `#BF5700` | `#f8f6f1` | 4.3 : 1 | AA (large text only); **not** AA for body text — use `#8a3d00` when the accent must carry text |
| `#6a6a72` | `#f8f6f1` | 4.8 : 1 | AA |

Rule of thumb: body text is graphite on warm-off-white. Burnt orange is an accent *shape*, not a text color.

## Private heritage note

Burnt orange is PMS 159 — UT Austin's official school color. The nod is intentional and symbolic. Public documentation, code, paper text, and repo contents **never** reference UT, UTexas, or bbooth@ — this is enforced by pre-commit hooks and CI checks across all public repos. The color carries the meaning silently; the words do not.
