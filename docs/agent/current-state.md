# Current State

## Objective

Keep the Manim repository easy for an agent to enter, with environment work,
scene work, and support material clearly separated.

## Current Structure

- `projects/normal-math-formula/` is the current active scene area.
- `skills/` is support/reference material.
- `legacy-output/` is the archived root-level output area from the older
  workflow.

## Current Decisions

- New render output should stay inside the subproject that produced it.
- The repository should not be restructured around a monolithic root output
  model again.
- `README.md` stays authoritative for environment setup.

## Next Likely Improvements

- Add new animation subprojects as self-contained folders.
- Keep active scene work under `projects/`.
- Retire or prune `legacy-output/` only when there is a deliberate cleanup
  task.
- Keep `Changing Description.txt` as historical record, not the primary agent
  handoff.
