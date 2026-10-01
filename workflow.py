"""Create and validate isolated Manim video projects."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VIDEO_ROOT = ROOT / "manim-video"


EPISODE_TEMPLATE = '''"""Episode source. Edit this file, then run it to render the complete video."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from manim import *


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "output"
QUALITY = {"low": "-ql", "medium": "-qm", "high": "-qh", "4k": "-qk"}


class Episode(Scene):
    def construct(self):
        title = Text("Replace with your opening", font_size=40)
        latex_formula = MathTex(r"e^{i\\pi} + 1 = 0")
        typst_formula = MathTypst("e^(i pi) + 1 = 0")
        formulas = VGroup(latex_formula, typst_formula).arrange(DOWN, buff=0.5)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP), Write(formulas))
        self.wait(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quality", choices=QUALITY, default="low")
    parser.add_argument("--preview", action="store_true")
    args = parser.parse_args()
    command = [
        sys.executable, "-m", "manim", QUALITY[args.quality],
        "--media_dir", str(OUTPUT_DIR), str(Path(__file__).resolve()), "Episode",
    ]
    if args.preview:
        command.append("--preview")
    return subprocess.run(command, cwd=PROJECT_DIR, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
'''


def create_project(name: str | None, requirement: str | None) -> int:
    name = (name if name is not None else input("Episode or series name: ")).strip()
    if not name or name in {".", ".."} or re.search(r'[<>:"/\\|?*]', name):
        print("Use a non-empty name without path separators or Windows filename characters.")
        return 2

    requirement = (requirement if requirement is not None else input("Video requirements / idea: ")).strip()
    if not requirement:
        print("Requirements cannot be empty.")
        return 2

    project_dir = VIDEO_ROOT / name.rstrip(" .")
    if project_dir.parent != VIDEO_ROOT or project_dir.exists():
        print(f"Project already exists or name is invalid: {project_dir}")
        return 2

    project_dir.mkdir(parents=True)
    (project_dir / "brief.md").write_text(
        f"# {name}\n\n## Requirements\n\n{requirement}\n",
        encoding="utf-8",
    )
    (project_dir / "episode.py").write_text(EPISODE_TEMPLATE, encoding="utf-8")
    print(f"Created: {project_dir}")
    print("Edit episode.py, then run it with the shared environment:")
    print(f'  .venv\\Scripts\\python.exe "{project_dir / "episode.py"}" --quality low')
    return 0


def check_environment() -> int:
    import manim
    import typst

    print(f"Python: {sys.version.split()[0]}")
    print(f"Manim: {manim.__version__}")
    print(f"Typst: {typst.__version__}")
    missing = [tool for tool in ("latex", "dvisvgm") if not _find_tool(tool)]
    if missing:
        print(f"Missing required tools: {', '.join(missing)}")
        return 1

    with tempfile.TemporaryDirectory(prefix=".check-", dir=VIDEO_ROOT) as temp:
        temp_dir = Path(temp)
        scene_file = temp_dir / "math_smoke.py"
        scene_file.write_text(
            "from manim import MathTex, MathTypst, Scene\n"
            "class MathSmoke(Scene):\n"
            " def construct(self):\n"
            "  self.add(MathTex(r'x^2 + 1'))\n"
            "  self.add(MathTypst('x^2 + 1'))\n",
            encoding="utf-8",
        )
        result = subprocess.run(
            [sys.executable, "-B", "-m", "manim", "-ql", "--media_dir", str(temp_dir / "output"), str(scene_file), "MathSmoke"],
            cwd=temp_dir,
            check=False,
        )
    if result.returncode:
        return result.returncode
    print("LaTeX and Typst render checks passed.")
    return 0


def _find_tool(name: str) -> str | None:
    import shutil

    return shutil.which(name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    new_parser = subparsers.add_parser("new", help="create a video folder")
    new_parser.add_argument("--name", help="episode or series name; prompts when omitted")
    new_parser.add_argument("--requirements", help="video idea and requirements; prompts when omitted")
    subparsers.add_parser("check", help="verify LaTeX and Typst rendering")
    args = parser.parse_args()
    VIDEO_ROOT.mkdir(exist_ok=True)
    if args.command == "new":
        return create_project(args.name, args.requirements)
    return check_environment()


if __name__ == "__main__":
    raise SystemExit(main())
