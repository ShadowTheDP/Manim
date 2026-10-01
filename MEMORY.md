# Manim Memory

## Stable Decisions

- One Manim Community Edition environment lives at `Project/Manim/.venv`.
- Manim is pinned to 0.21.0; Typst is pinned to 0.15.0.
- Both LaTeX (`MathTex`, `Tex`) and Typst (`MathTypst`, `Typst`) are supported.
- Each episode or series owns one folder under `manim-video/`; its source,
  assets, brief, generated video, and Manim intermediates stay in that folder.
- A video's `episode.py` is its direct render entrypoint.
- `workflow.py` is only the root orchestrator: `new` creates a video folder and
  `check` verifies the shared math renderers.
- Source is synchronized with `https://github.com/ShadowTheDP/Manim` on `main`.
- Keep `.venv/` and generated episode `output/` directories out of Git.
- Production episodes render at 1080p60 by default (`--quality high`); only
  `episode-test` uses low quality.

## Canonical Commands

Create a video folder (prompts for omitted values):

```powershell
.\.venv\Scripts\python.exe workflow.py new
```

Check the shared runtime and both math renderers:

```powershell
.\.venv\Scripts\python.exe workflow.py check
```

Render a production video at 1080p60:

```powershell
.\.venv\Scripts\python.exe "manim-video\<name>\episode.py"
```

Known working example:

```powershell
.\.venv\Scripts\python.exe manim-video\episode-test\episode.py --quality low
```

## Reusable Guidance

- Use `skills/manim-composer/SKILL.md` to plan educational video narratives.
- Use `skills/manimce-best-practices/SKILL.md` for ManimCE code patterns.
- Use `skills/typst-manim/SKILL.md` when choosing LaTeX vs Typst or composing
  mathematical objects.
- FFmpeg is unnecessary for Manim 0.21 core rendering and common
  `Scene.add_sound()` audio muxing; add it for an external conversion pipeline,
  unsupported codecs, or tools that explicitly invoke the FFmpeg CLI.
