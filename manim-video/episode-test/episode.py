"""Episode source. Edit this file, then run it to render the complete video."""

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
        latex_formula = MathTex(r"e^{i\pi} + 1 = 0")
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
