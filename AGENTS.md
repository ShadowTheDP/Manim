# Manim Agent Instructions

## Entry Order

1. `README.md`
2. `MEMORY.md`
3. `docs/agent/current-state.md`
4. Relevant skill under `skills/`
5. The selected project under `manim-video/`

## Workflow

- For a new video, ask the user for its episode/series name and requirements.
- Create the project with the shared interpreter and the user's answers:
  `.venv\Scripts\python.exe workflow.py new --name "..." --requirements "..."`.
  The CLI also prompts for omitted values. Keep its brief, source, assets, and
  all generated output inside `manim-video/<name>/`.
- Use the shared root `.venv` for every Manim project.
- The runnable `episode.py` must render the complete video when executed.
- Support both LaTeX (`MathTex`, `Tex`) and Typst (`MathTypst`, `Typst`).
- Read `manim-composer` for educational narrative planning and
  `manimce-best-practices` for Community Edition implementation. Use
  `typst-manim` for math syntax and mixed LaTeX/Typst guidance.
- Use the project Git repository for source synchronization with
  `https://github.com/ShadowTheDP/Manim`. Do not initialize nested repositories
  under `manim-video/`.
- Do not commit `.venv/` or generated `output/` media; `.gitignore` owns that
  boundary.
- Keep shared workflow code and handoff documents at the project root; video
  sources, assets, and render outputs stay in the selected video folder.

## Validation

- Environment and LaTeX/Typst render check:
  `.venv\Scripts\python.exe workflow.py check`
- Render a video by running its own entry file:
  `.venv\Scripts\python.exe manim-video\<name>\episode.py --quality low`
