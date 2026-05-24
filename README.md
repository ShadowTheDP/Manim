# Manim

## Purpose

This repository is for writing and rendering Manim videos.

This repo may contain smaller animation subprojects over time.

The highest priority here is a reliable Manim runtime environment so that a
future human or AI agent can focus on scene and content production instead of
rebuilding the toolchain from scratch.

## What "Correct Work" Means Here

Human collaborators and AI agents should treat this repo as a video-authoring
workspace.

Correct ways to work on this project:

- Add scene code in a clearly named file or subproject folder.
- Keep reusable support material in `skills/`.
- Keep environment notes and setup instructions accurate in this README.
- Prefer descriptive scene class names so render commands stay obvious.
- Prefer repo-relative paths and short, reproducible render commands.
- Check existing `skills/` guidance before inventing new Manim patterns.
- Keep the render environment dependable before optimizing scene content.
- For new small subprojects, keep generated output inside the subproject that
  produced it.

Avoid:

- Checking virtual environment contents into Git.
- Mixing generated render output with source scene files.
- Treating support-skill content as end-user video source code.
- Writing project files outside this repository.
- Adding dependencies without documenting them in `requirements.txt`.
- Adding README files to small animation subprojects. The parent README should
  stay authoritative.
- Confusing skill/reference folders with animation subprojects. Skill folders
  may keep documentation because they are support material, not project work
  areas.

## Environment

Current expectation:

- Python 3.12
- Project-local virtual environment: `.venv/`
- Main package: `manim==0.19.2`

If the virtual environment does not exist yet, create it with:

```powershell
py -3.12 -m venv .venv
```

Activate the local environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install dependencies if needed:

```powershell
python -m pip install -r requirements.txt
```

Practical environment rules:

- Prefer Windows PowerShell-friendly, non-interactive commands.
- If activation is blocked by PowerShell policy, use:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- If `pip` or `pip.exe` behaves oddly, prefer:

```powershell
python -m pip install -r requirements.txt
```

- If VS Code selects the wrong interpreter, use `Python: Select Interpreter`
  and choose the project's `.venv`.
- If the project folder is moved, the safest assumption is to recreate
  `.venv/`.
- If you add or change dependencies, update `requirements.txt` in the same
  task.

## MathTex and LaTeX Notes

MathTex rendering depends on an external LaTeX toolchain.

Current expectation:

- `latex.exe` available
- `dvisvgm.exe` available
- `ffmpeg.exe` available
- MiKTeX recommended on Windows
- Ghostscript can be useful for some LaTeX or SVG-related edge cases

If MiKTeX is installed but not visible in the current shell, a temporary PATH
fix can look like:

```powershell
$env:PATH = 'C:\Program Files\MiKTeX\miktex\bin\x64;' + $env:PATH
latex --version
dvisvgm --version
```

If you want to persist that PATH change for the current Windows user:

```powershell
setx PATH "C:\Program Files\MiKTeX\miktex\bin\x64;%PATH%"
```

If MathTex or LaTeX rendering breaks, solve the environment first before
changing scene content.

## First Useful Commands

Check the environment:

```powershell
python normal-math-formula/test_env.py
```

This script is an offline dependency check. It verifies Python package imports
and required external tools such as `latex`, `dvisvgm`, and `ffmpeg`.

Verify minimal MathTex rendering:

```powershell
manim normal-math-formula/tesr.py SimpleTex -pql
```

Render a simple sample scene:

```powershell
manim normal-math-formula/example.py BasicMathFormula -pql
```

Render the binomial theorem example:

```powershell
manim normal-math-formula/binomial-theorem.py BinomialTheorem -pql
```

## Inputs

Typical inputs for this repo are:

- Scene files under `normal-math-formula/`
- New animation subprojects in their own folders
- Reusable AI-agent guidance under `skills/`

If you add a larger or more focused animation subproject, prefer a structure
like:

```text
project-name/
  scenes.py
  assets/
  output/
```

Small subprojects should not get their own README. Keep their purpose obvious
through naming, file layout, and this parent README.

Skill/reference folders under `skills/` are the explicit exception because they
exist to help humans or AI agents work on the main project rather than to serve
as video subprojects.

## Outputs

Output policy depends on whether work lives at the repo root or inside a
subproject:

- For small subprojects, put output inside that subproject.
- For direct local experiments, Manim may also create local `media/` folders.
- The root-level `output/` directory is now best treated as older shared output
  from an earlier workflow, not the preferred default for new subprojects.

Examples:

```text
normal-math-formula/media/
project-name/output/
```

Legacy root-level output may still contain:

- `videos/` for rendered scene output
- `images/` for exported still images or thumbnails
- `Tex/` for LaTeX and MathTex intermediate artifacts
- `texts/` for generated text-related artifacts

If older output-side files such as `Changing-Description.txt` exist, treat them
as legacy local artifacts rather than the official project change log.

## File Map

Top-level files and folders:

- `.gitignore`
  - Git ignore rules for Python artifacts, output, and local editor files.
- `README.md`
  - This project working guide and the single source of truth for workflow
    rules.
- `Changing Description.txt`
  - The single official project change log. Update it after completed work,
    especially before pushing to GitHub.
- `requirements.txt`
  - Python dependencies for the Manim environment.
- `.venv/`
  - Local virtual environment. Useful locally, not project source.
- `normal-math-formula/`
  - Current example subproject for small Manim experiments and environment
    checks.
- `skills/`
  - AI-agent support skills, references, templates, and examples.
- `output/`
  - Older shared render output from an earlier workflow. Not the preferred
    default for new subprojects.

Files inside `normal-math-formula/`:

- `example.py`
  - Collection of basic Manim math and animation examples.
- `binomial-theorem.py`
  - Example scene that presents and expands the binomial theorem.
- `test_env.py`
  - Offline environment sanity-check script for Python packages and required
    external render tools.
- `tesr.py`
  - Minimal MathTex smoke-test scene used to verify LaTeX rendering works.
- `media/`
  - Local Manim-generated intermediate or rendered output for this subproject.
  - Disposable, not source code.
- `__pycache__/`
  - Python bytecode cache. Disposable, not project source.

Inside `skills/`:

- `manim-composer/`
  - AI-agent guidance for composing video scenes and narratives.
- `manimce-best-practices/`
  - AI-agent best-practice material for Manim Community Edition.
- `manimgl-best-practices/`
  - AI-agent best-practice material for ManimGL.

These `skills/` folders are support material, not normal end-user render
targets.

## Troubleshooting Shortlist

If rendering fails, check these in order:

1. Is `.venv/` activated?
2. Does `python normal-math-formula/test_env.py` report `manim`, `latex`,
   `dvisvgm`, and `ffmpeg` as available?
3. Does `manim normal-math-formula/tesr.py SimpleTex -pql` work?
4. Are `latex.exe`, `dvisvgm.exe`, and `ffmpeg.exe` available in `PATH`?
5. If a render directory contains broken partial output, remove the relevant
   `partial_movie_files/<Scene>/` folder and rerun.

## Working Rules for AI Agents

If you are an AI agent working in this repo:

1. Read this README first.
2. Treat this README as the single source of truth for working rules.
3. Stay inside `Project/Manim/` unless a human explicitly asks otherwise.
4. Decide whether you are editing a real video source file or only support
   material in `skills/`.
5. Prefer subproject-local output over root-level output for new work.
6. Do not edit `.venv/`.
7. Prefer repo-relative paths in commands, docs, and scripts.
8. Consult relevant material in `skills/` before changing scene architecture or
   animation style assumptions.
9. If you add a new dependency, record it in `requirements.txt`.
10. If you create or modify a scene, prefer including a quick low-quality render
    command such as `-pql` in your notes or verification steps.
11. If the environment is broken, fix the environment before changing scene
    content.
12. Update `Changing Description.txt` after meaningful completed work,
    especially before push.
13. Do not add README files to small animation subprojects.
14. Skill/reference folders may keep their own documentation when that
    documentation exists only to support the main project workflow.

## Before Push Checklist

Before pushing to GitHub, check:

- No files from `.venv/` were added.
- Generated renders are not mixed into source folders.
- New scene files have descriptive names.
- Support-material changes in `skills/` were intentional.
- New dependencies were documented in `requirements.txt`.
- `Changing Description.txt` was updated to reflect the completed work.
- README updates were included if the project structure changed.

## Current Gaps

- `normal-math-formula/tesr.py` uses a legacy filename and may deserve a later
  rename if you want cleaner naming.
