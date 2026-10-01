# Manim Video Workspace

This folder is the single entrypoint for creating complete Manim videos. Use
Manim Community Edition 0.21 with one shared `.venv`; LaTeX and Typst are both
supported for mathematical content.

The workflow files use `manim-video/`. Legacy videos, examples, and old ManimGL
guidance have been removed. The source workflow is synchronized with the
GitHub repository `ShadowTheDP/Manim`.

## What `workflow.py` Does

`workflow.py` is the root orchestration entrypoint. It does not contain a
video scene and does not replace an episode. It has two small jobs:

- `new`: ask for or accept the video name and requirements, then create one
  self-contained `manim-video/<name>/` folder with `brief.md` and `episode.py`.
- `check`: render one LaTeX expression and one Typst expression to verify the
  shared environment.

The generated `episode.py` is the actual video program. Running it calls Manim
with the shared `.venv` and writes all output into its own folder.

## Start Here

From `Project/Manim`, create an episode or series folder:

```powershell
.\.venv\Scripts\python.exe workflow.py new
```

The command asks for a name and the video requirements, then creates:

```text
manim-video/<episode-or-series>/
  brief.md
  episode.py
```

There is a working reference at `manim-video/episode-test/`. Run it directly:

```powershell
.\.venv\Scripts\python.exe manim-video\episode-test\episode.py --quality low
```

The agent develops the requested video in that folder, using the `manim-composer`
skill for narrative planning and `manimce-best-practices` plus
`typst-manim` for Manim and math implementation. Add assets or episode scenes
beside `episode.py` when needed. All render artifacts and intermediate files
belong under that folder's `output/`.

Run the file to render the complete episode:

```powershell
.\.venv\Scripts\python.exe "manim-video\<name>\episode.py" --quality low
```

Use `medium`, `high`, or `4k` for higher quality. Add `--preview` to open the
rendered video. Each episode uses the root `.venv`; do not create a separate
virtual environment inside `manim-video/`.

## Environment

- Python 3.13
- `manim==0.21.0`
- `typst==0.15.0`
- LaTeX through `latex.exe` and `dvisvgm.exe` for `MathTex` and `Tex`
- `MathTypst` and `Typst` for Typst-authored formulas and markup

Check that both math paths render:

```powershell
.\.venv\Scripts\python.exe workflow.py check
```

Manim 0.21 uses PyAV for video encoding, partial-video assembly, and common
audio muxing through `Scene.add_sound()`. FFmpeg is not a core prerequisite;
install it only when an external tool, unsupported codec, or separate media
conversion pipeline explicitly needs the FFmpeg command line.

Install the shared environment only if it is missing or damaged:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Agent Handoff

1. Read `README.md`, `AGENTS.md`, `MEMORY.md`, and
   `docs/agent/current-state.md`.
2. For a new video, ask the user for the episode/series name and requirements.
3. Pass those answers to `workflow.py new --name ... --requirements ...`.
   Either option may be omitted when using the terminal prompts directly.
4. Preserve the brief in the new folder and write all video-specific source
   and assets inside it.
5. Read `skills/manim-composer/SKILL.md` when shaping an educational narrative.
   Read the relevant ManimCE and math guidance before implementation.
6. Render by executing that folder's `episode.py` with the root `.venv`.
7. Keep every generated file inside that episode folder. Do not use a project
   Git repository or create per-video environments.

## Layout

- `workflow.py`: create a new video folder and check both math renderers; it is
  the only root-level production entrypoint.
- `manim-video/`: all episode and series projects, source, assets, and outputs.
- `.venv/`: the single shared Manim runtime.
- `skills/`: reusable agent guidance; not video output.
- `docs/agent/`: workspace handoff state.
- `Changing Description.txt`: current workflow reset record.
- `.gitignore`: keeps the shared environment and generated media out of Git.
