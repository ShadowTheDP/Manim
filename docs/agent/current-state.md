# Current State

## Objective

Provide one shared Manim 0.21 environment and a repeatable workflow where each
episode or series is a self-contained folder with a directly executable video
entrypoint.

## Structure

- `workflow.py` prompts for a new video name and requirements, creates a folder,
  and verifies the shared LaTeX/Typst render toolchain.
- `manim-video/` is the only home for video-specific source, assets, and output.
- `manim-video/episode-test/` is the current working reference and renders a
  small scene containing both LaTeX and Typst formulas.
- `.venv/` is the only Manim environment.
- `skills/` contains reusable agent guidance.
- Source synchronization is enabled through
  `https://github.com/ShadowTheDP/Manim` on `main`.
- Old projects, legacy output, root media, ManimGL-only guidance, and the old
  generated media have been removed. `.gitignore` excludes the shared `.venv`
  and episode outputs. Use only `manim-video/` for new videos.

## Runtime

- Python 3.13
- Manim Community 0.21.0
- Production episodes use `-qh` / 1080p60 by default; `episode-test` is the
  only low-quality exception.
- Typst 0.15.0
- LaTeX is required for `MathTex`/`Tex`; Typst is available through `MathTypst`/`Typst`.
- FFmpeg is optional for Manim 0.21 core rendering and common audio muxing;
  install it only for external conversion, unsupported codecs, or tools that
  explicitly invoke the FFmpeg CLI.

## New Video Flow

1. Ask the user for the episode/series name and requirements.
2. Run `workflow.py new --name "..." --requirements "..."` with those answers.
3. Develop `manim-video/<name>/episode.py`, keeping assets and notes beside it.
4. Execute that `episode.py` with the root `.venv`; its output goes into the
   same video's `output/` directory.

The root-level `workflow.py` is orchestration only; the episode file is the
program that produces the video.

## Skills

- `manim-composer`: educational narrative and scene planning.
- `manimce-best-practices`: Manim Community implementation reference.
- `typst-manim`: choosing and composing LaTeX and Typst math.
