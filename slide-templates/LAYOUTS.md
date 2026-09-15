# Slide layout templates

Six canonical layouts for the Quarto reveal.js course decks (1920×1080, `custom.scss`).
`layout-templates.qmd` in this directory renders one slide per layout from real course
figures — `quarto render layout-templates.qmd` and open the HTML to see them.

The showcase is built with the VisML theme. The InfoVis theme differs cosmetically (colours,
spacing — ~55 lines of `custom.scss`) but defines the same `.smaller`, and every sizing rule
below is Quarto/reveal behaviour rather than theme, so the layouts apply to both courses unchanged.

The rules came from a census of the 2026 VisML week 3 decks (59 slides), not from taste.
Three findings drive everything:

- **Quarto auto-stretches almost every single-image slide** to fill the remaining *height*,
  whether or not text sits above or below the figure. So what varies is *width* used, and that
  is set by the figure's aspect ratio: wide figures fill ~91% of the slide, landscape ~64%,
  **square ~45%, tall ~35%**. A square figure with one bullet above it is the dead-space case.
- **Figure shape, not text amount, chooses the layout.** Measure aspect ratio first.
- **The decks already have an idiom** — `.columns` with `{.column width="NN%"}` (50/50, then
  40/60), `width="NN%"`, `fig-align`. These templates use only that vocabulary.

## Choosing a layout

Aspect ratio (AR) = width ÷ height of the image file (`sips -g pixelWidth -g pixelHeight f.jpg`).

| Figure | Body text | Layout |
|---|---|---|
| wide (AR ≥ 1.8) or landscape (1.2–1.8) | none | **L1** full-bleed |
| wide or landscape | one line | **L2** statement + figure |
| wide | two or more lines | **L2** — trim to one line, rest to speaker notes |
| landscape | two or more lines | **L3** with `width="100%"` |
| square (0.8–1.2) or tall (< 0.8) | any text | **L3** with `height="760"` |
| square or tall | none | **L4** centred, `.nostretch` |
| two figures | — | **L5** comparison |
| no figure | ≤ 6 bullets | **L6** single column |
| no figure | 7+ bullets | **L6** two `.smaller` columns |

## The six layouts

### L1 · Full-bleed figure

```markdown
## Title

![](figs/wide-figure.jpg){fig-align="center"}
```

One image, nothing else. Auto-stretch sizes it. Put attribution in a `::: footer` block, not the body.

### L2 · Statement + figure

```markdown
## Title

**One sentence, bold, that the figure demonstrates.**

![](figs/wide-or-landscape.jpg){fig-align="center"}
```

Exactly one line. A second line costs ~50px of figure height and reads as an orphan;
move it to speaker notes.

### L3 · Text beside figure (40 / 60)

```markdown
## Title

:::: {.columns}
::: {.column width="40%"}
* two or three bullets
* the figure's implication
:::
::: {.column width="60%"}
![](figs/square-figure.jpg){height="760" fig-align="center"}
:::
::::
```

For a **landscape** figure in the right column use `{width="100%" fig-align="center"}` instead —
760px tall is wider than a 60% column for AR > 1.45. Wants 2–3 bullets on the left; one bullet
in a 40% column looks sparse — promote a sentence from the speaker notes.

### L4 · Centred figure

```markdown
## Title

![](figs/square-figure.jpg){.nostretch width="55%" fig-align="center"}
```

`.nostretch` is **required**. Without it Quarto still applies auto-stretch and reveal's stretch
script overrides the width at runtime.

Derive the width from the aspect ratio so the figure stays inside the ~880px below the heading:
**width% ≈ 48 × AR, rounded down to a multiple of 5, capped at 55.** A true square (AR 1.0) gets
45%; AR 1.14 gets 50%; a tall 0.7 cover gets 30%. `55%` on a square figure overflows the slide.

### L5 · Comparison

```markdown
## Title

:::: {.columns}
::: {.column width="50%"}
![](figs/before.jpg){width="100%"}
:::
::: {.column width="50%"}
![](figs/after.jpg){width="100%"}
:::
::::

**One bold caption saying what differs.**
```

Stacked variant (a wide figure over its result): two bare images, both `.nostretch` with
`fig-align="center"`, `width="90%"` then `width="55%"`. Check the sum of the two rendered heights
(1840 × width ÷ AR each) stays under ~850px; 100%/62% overflows for the Cleveland–McGill pair.

### L6 · Text only

```markdown
## Title

:::: {.columns .smaller}
::: {.column width="50%"}
* four bullets
:::
::: {.column width="50%"}
* four bullets
:::
::::
```

Single column up to six bullets. Split at seven so nothing shrinks past `.smaller` (0.9em).
Split only **flat** lists: a nested list (a bullet with sub-bullets) does not divide evenly and
reads worse in two columns — leave it single-column, or flatten it first.

## Sizing facts that are easy to get wrong

Verified by rendering against the real theme (Quarto 1.10.18):

- `width="55%"` on a lone image does **not** disable auto-stretch; add `.nostretch`.
- Images inside `.columns` never auto-stretch. There, `width="100%"` means 100% **of the
  column** with height uncapped — a square figure in a 60% column overflows the slide.
- `height="760"` works inside columns: Quarto emits it as an HTML `height` attribute and the
  theme only caps `max-width/max-height: 95%`, so the browser honours it.
- Do not indent an image under a bullet (`  ![](...)`). It becomes a list-item child, escapes
  auto-stretch, and renders at raw pixel size.
- `fig-align="center"` reliably centres (`quarto-figure-center`). Nothing else needs it.

## Applying to an existing deck

Measure every figure's AR, count body lines per slide, map with the table above. In the
week 3 decks this moved 17 of 19 dead-space slides to L3/L4 and touched ~30 slides in all.
Do it with the deck off the projector — it improves what students read afterwards, not
what you say in the room. Add new slides rather than restructuring on the day of class.
