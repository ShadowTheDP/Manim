---
name: typst-manim
description: >
  Trigger when authoring mathematical content in Manim Community Edition,
  choosing between LaTeX and Typst, or creating a complete episode in
  manim-video/. This project uses Manim 0.21 with both renderers installed.
---

## Role

Use Manim for timing, motion, grouping, and video output. Math may be authored
in either LaTeX or Typst in the same episode. Keep the runnable scene and its
generated output inside the selected `manim-video/<name>/` folder.

## LaTeX

- Use `MathTex` for mathematical expressions and `Tex` for LaTeX text.
- Raw strings (`r"..."`) avoid Python escaping LaTeX backslashes.
- Use `MathTex(..., substrings_to_isolate=[...])` or explicit argument groups
  when parts need separate styling or animation.
- LaTeX requires `latex.exe` and `dvisvgm.exe`; the shared environment check
  verifies actual rendering.

## Typst

- Use `MathTypst` for display mathematics and `Typst` for general markup.
- Write Typst syntax inside these objects, not LaTeX syntax.
- Use `{{ expression : label }}` groups when a subexpression needs independent
  animation or color, then select it with `equation.select("label")`.
- The Python `typst` package compiles Typst to SVG; a separate Typst CLI is not
  needed.

## Choosing A Format

- Use the source's native format when animating an existing document or proof.
- Prefer Typst for new formula-heavy scripts when its syntax is comfortable to
  the author.
- Use LaTeX when relying on LaTeX-specific commands, packages, or existing
  MathTex substring workflows.
- Keep each expression in one format. Do not pass LaTeX commands to Typst or
  Typst operators to `MathTex`.

## Episode Flow

1. Read the project brief and outline the narrative using `manim-composer` for
   educational videos.
2. Implement the complete entrypoint in `manim-video/<name>/episode.py`.
3. Run it with the root `.venv` at low quality, then raise quality for final
   output. The entrypoint routes Manim's videos, vectors, and intermediates to
   its local `output/` directory.
4. Run `python workflow.py check` if either formula renderer fails.
