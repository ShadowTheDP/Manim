"""A visual derivation of the Gaussian integral."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np
from manim import *


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "output"
QUALITY = {"low": "-ql", "medium": "-qm", "high": "-qh", "4k": "-qk"}


class GaussianIntegral(Scene):
    """Derive integral exp(-x^2) over the real line using polar coordinates."""

    def setup(self):
        self.camera.background_color = "#10131A"

    @staticmethod
    def formula(source: str, size: float = 48, color=WHITE) -> MathTex:
        return MathTex(source, font_size=size, color=color)

    def construct(self):
        self.introduction()
        self.square_the_integral()
        self.polar_coordinates()
        self.separate_and_evaluate()
        self.conclusion()

    def introduction(self):
        title = Text("Gaussian Integral", font_size=48, color=TEAL_A)
        subtitle = Text("Finding the area under a curve with no elementary antiderivative", font_size=24)
        subtitle.scale_to_fit_width(11.5)
        target = self.formula(r"I=\int_{-\infty}^{\infty}e^{-x^2}\,dx", 62, YELLOW)
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.35)

        axes = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[0, 1.1, 0.5],
            x_length=8.4,
            y_length=3.8,
            axis_config={"color": GREY_B, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 0.45)
        curve = axes.plot(lambda x: np.exp(-(x**2)), x_range=[-3, 3], color=BLUE_C, stroke_width=4)
        area = axes.get_area(curve, x_range=[-3, 3], color=BLUE_E, opacity=0.5)
        label = Text("the total area", font_size=25, color=BLUE_B).next_to(axes, DOWN, buff=0.18)

        self.play(FadeIn(header, shift=DOWN))
        self.play(Write(target))
        self.play(Create(axes), Create(curve), FadeIn(area), FadeIn(label))
        self.wait(1.2)
        self.play(FadeOut(header), FadeOut(label), target.animate.to_edge(UP, buff=0.3))
        self.gaussian_axes = VGroup(axes, curve, area)
        self.target_formula = target

    def square_the_integral(self):
        square = self.formula(
            r"I^2=\left(\int_{-\infty}^{\infty}e^{-x^2}\,dx\right)"
            r"\left(\int_{-\infty}^{\infty}e^{-y^2}\,dy\right)",
            38,
        )
        square.scale_to_fit_width(12.2).to_edge(UP, buff=0.25)
        self.play(ReplacementTransform(self.target_formula, square))

        left_target = self.gaussian_axes.copy().scale(0.52).to_edge(LEFT, buff=0.5).shift(DOWN * 0.45)
        right_target = self.gaussian_axes.copy().scale(0.52).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.45)
        self.play(Transform(self.gaussian_axes, left_target), FadeIn(right_target, shift=RIGHT))

        double = self.formula(r"I^2=\iint_{\mathbb{R}^2}e^{-(x^2+y^2)}\,dx\,dy", 48, YELLOW)
        double.scale_to_fit_width(11.8).move_to(square)
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5.5,
            y_length=5.5,
            background_line_style={"stroke_opacity": 0.22},
            axis_config={"color": GREY_B, "stroke_width": 2},
        ).shift(DOWN * 0.35)
        x_label = MathTex("x", font_size=32).next_to(plane.x_axis.get_end(), RIGHT)
        y_label = MathTex("y", font_size=32).next_to(plane.y_axis.get_end(), UP)
        plane_caption = Text("the whole plane", font_size=25, color=BLUE_B).next_to(plane, DOWN, buff=0.12)

        self.play(ReplacementTransform(square, double), FadeOut(self.gaussian_axes), FadeOut(right_target))
        self.play(Create(plane), Write(x_label), Write(y_label), FadeIn(plane_caption))
        self.wait(1.2)
        self.square_formula = double
        self.plane = plane
        self.plane_labels = VGroup(x_label, y_label, plane_caption)

    def polar_coordinates(self):
        polar = self.formula(
            r"x=r\cos\theta,\qquad y=r\sin\theta,\qquad "
            r"x^2+y^2=r^2,\qquad dx\,dy=r\,dr\,d\theta",
            38,
        )
        polar.scale_to_fit_width(12.2).to_edge(UP, buff=0.25)
        self.play(ReplacementTransform(self.square_formula, polar))

        origin = self.plane.c2p(0, 0)
        rings = VGroup()
        for radius in np.linspace(2.8, 0.35, 9):
            opacity = 0.045 + 0.13 * np.exp(-(radius**2) / 2)
            rings.add(
                Circle(
                    radius=radius * 0.88,
                    color=BLUE_C,
                    stroke_width=1.5,
                    stroke_opacity=0.28,
                    fill_color=BLUE_E,
                    fill_opacity=opacity,
                ).move_to(origin)
            )

        radial_line = Line(origin, self.plane.c2p(2.25, 1.5), color=YELLOW, stroke_width=4)
        angle_arc = Arc(radius=0.68, start_angle=0, angle=np.arctan2(1.5, 2.25), color=ORANGE, stroke_width=4)
        angle_arc.move_to(origin)
        r_label = MathTex("r", font_size=34, color=YELLOW).next_to(radial_line.get_end(), RIGHT, buff=0.08)
        theta_label = MathTex(r"\theta", font_size=34, color=ORANGE).next_to(origin + RIGHT * 0.65 + UP * 0.15)
        symmetry = Text("rotation symmetry", font_size=25, color=TEAL_A).to_edge(DOWN, buff=0.3)

        self.play(LaggedStart(*[FadeIn(ring) for ring in rings], lag_ratio=0.08, run_time=1.6))
        self.play(Create(radial_line), Create(angle_arc), Write(r_label), Write(theta_label), FadeIn(symmetry))
        self.wait(1)

        polar_integral = self.formula(
            r"I^2=\int_{0}^{2\pi}\int_{0}^{\infty}e^{-r^2}\,r\,dr\,d\theta",
            48,
            YELLOW,
        )
        polar_integral.scale_to_fit_width(11.8).move_to(polar)
        self.play(ReplacementTransform(polar, polar_integral))
        self.wait(1)

        self.rings = VGroup(self.plane, self.plane_labels, rings, radial_line, angle_arc, r_label, theta_label, symmetry)
        self.polar_formula = polar_integral

    def separate_and_evaluate(self):
        separate = self.formula(
            r"I^2=\left(\int_{0}^{2\pi}d\theta\right)"
            r"\left(\int_{0}^{\infty}r e^{-r^2}\,dr\right)",
            42,
            YELLOW,
        )
        separate.scale_to_fit_width(12.1).to_edge(UP, buff=0.25)
        self.play(ReplacementTransform(self.polar_formula, separate), FadeOut(self.rings))

        angle_title = Text("angle", font_size=28, color=ORANGE)
        angle_work = self.formula(r"\int_{0}^{2\pi}d\theta=[\theta]_{0}^{2\pi}=2\pi", 42)
        angle_group = VGroup(angle_title, angle_work).arrange(DOWN, buff=0.3).to_edge(LEFT, buff=0.55).shift(DOWN * 0.5)

        radius_title = Text("radius", font_size=28, color=BLUE_B)
        substitution = self.formula(r"u=r^2,\qquad du=2r\,dr", 40)
        radius_work = self.formula(
            r"\int_{0}^{\infty}r e^{-r^2}\,dr"
            r"=\frac12\int_{0}^{\infty}e^{-u}\,du=\frac12",
            36,
        )
        radius_work.scale_to_fit_width(5.5)
        radius_group = VGroup(radius_title, substitution, radius_work).arrange(DOWN, buff=0.28)
        radius_group.to_edge(RIGHT, buff=0.45).shift(DOWN * 0.42)

        self.play(FadeIn(angle_group, shift=UP), FadeIn(radius_group, shift=UP))
        self.wait(1.4)

        combined = self.formula(r"I^2=2\pi\cdot\frac12=\pi", 54, YELLOW)
        combined.to_edge(UP, buff=0.3)
        self.play(ReplacementTransform(separate, combined), FadeOut(angle_group), FadeOut(radius_group))
        self.play(Circumscribe(combined, color=YELLOW, time_width=1.5))
        self.wait(1)
        self.combined_formula = combined

    def conclusion(self):
        answer = self.formula(
            r"I=\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}",
            58,
            YELLOW,
        )
        answer.scale_to_fit_width(12.2)
        note = Text("The square root is positive because the Gaussian is positive.", font_size=28, color=TEAL_A)
        note.scale_to_fit_width(11.8).next_to(answer, DOWN, buff=0.5)
        self.play(ReplacementTransform(self.combined_formula, answer))
        self.play(FadeIn(note, shift=UP))
        self.wait(2)
        self.play(Circumscribe(answer, color=BLUE_C, time_width=2))
        self.wait(1.5)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quality", choices=QUALITY, default="high")
    parser.add_argument("--preview", action="store_true")
    args = parser.parse_args()
    command = [
        sys.executable,
        "-m",
        "manim",
        QUALITY[args.quality],
        "--media_dir",
        str(OUTPUT_DIR),
        str(Path(__file__).resolve()),
        "GaussianIntegral",
    ]
    if args.preview:
        command.append("--preview")
    return subprocess.run(command, cwd=PROJECT_DIR, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
