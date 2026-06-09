# Manim AGENTS

## Read Order

1. `README.md`
2. `docs/agent/current-state.md`
3. `Changing Description.txt` only when historical render or environment detail
   matters
4. The target scene subproject under `projects/`
5. `skills/` only when the task is about reusable Manim guidance

## Scope

- Stay inside `Project/Manim/`.
- Treat this repository as a video-authoring workspace, not a generic Python
  sandbox.
- Prefer subproject-local outputs over repo-root output.

## Default Ignore Paths

- `.venv/`
- `legacy-output/` unless the task is explicitly about legacy output cleanup
- `**/__pycache__/`
- rendered media not needed for the current task

## Preferred Plugins

- `Everything MCP` for file discovery
- `QMD` for local documentation and handoff docs
- `GitHub MCP` for repo history or remote review
- `Context7` for Manim or Python-library docs

## Validation

Use the narrowest command that proves the change:

- `python projects/normal-math-formula/test_env.py`
- `manim projects/normal-math-formula/tesr.py SimpleTex -pql`
- task-specific render commands from `README.md`

## Structure Direction

- Keep each animation effort in its own folder under `projects/`.
- Treat `legacy-output/` as archived history and do not add new generated work
  there.
- Keep `skills/` as support material, not production scene output.
