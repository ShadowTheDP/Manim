from manim import *

class BasicMathFormula(Scene):
    def construct(self):
        formula = MathTex(r"E = mc^2")
        self.play(Write(formula))
        self.wait()

class MultiLineFormula(Scene):
    def construct(self):
        formula = MathTex(
            r"(a + b)^2 &= a^2 + 2ab + b^2 \\"
            r"(a - b)^2 &= a^2 - 2ab + b^2 \\"
        )
        self.play(Write(formula))
        self.wait()

class SubSupScript(Scene):
    def construct(self):
        formula = MathTex(r"x_1^2 + y_1^2 = r^2")
        self.play(Write(formula))
        self.wait()

class FractionExample(Scene):
    def construct(self):
        formula = MathTex(r"\frac{1}{2} + \frac{1}{4} = \frac{3}{4}")
        self.play(Write(formula))
        self.wait()

class SquareRootExample(Scene):
    def construct(self):
        formula = MathTex(r"\sqrt{16} = 4")
        self.play(Write(formula))
        self.wait()

class IntegralExample(Scene):
    def construct(self):
        formula = MathTex(r"\int_a^b f(x) \, dx")
        self.play(Write(formula))
        self.wait()

class MatrixExample(Scene):
    def construct(self):
        formula = MathTex(
            r"\begin{bmatrix}"
            r"1 & 2 & 3 \\"
            r"4 & 5 & 6 \\"
            r"7 & 8 & 9"
            r"\end{bmatrix}"
        )
        self.play(Write(formula))
        self.wait()

class GreekLettersExample(Scene):
    def construct(self):
        formula = MathTex(r"\alpha, \beta, \gamma, \delta")
        self.play(Write(formula))
        self.wait()

class SpecialSymbolsExample(Scene):
    def construct(self):
        formula = MathTex(r"\infty, \pm, \leq, \geq")
        self.play(Write(formula))
        self.wait()

class AlignExample(Scene):
    def construct(self):
        formula = MathTex(
            r"x &= y + z \\"
            r"a &= b + c \\"
        )
        self.play(Write(formula))
        self.wait()

class ColorExample(Scene):
    def construct(self):
        formula = MathTex(r"x^2 + y^2 = z^2", substrings_to_isolate=["x", "y", "z"])
        formula.set_color_by_tex("x", RED)
        formula.set_color_by_tex("y", GREEN)
        formula.set_color_by_tex("z", BLUE)
        self.play(Write(formula))
        self.wait()

class TransformExample(Scene):
    def construct(self):
        formula1 = MathTex(r"x^2 + y^2 = z^2")
        formula2 = MathTex(r"a^2 + b^2 = c^2")
        self.play(Write(formula1))
        self.wait()
        self.play(Transform(formula1, formula2))
        self.wait()

class GroupExample(Scene):
    def construct(self):
        formula1 = MathTex(r"x + y = z")
        formula2 = MathTex(r"a + b = c")
        group = VGroup(formula1, formula2).arrange(DOWN)
        self.play(Write(group))
        self.wait()

class PositionExample(Scene):
    def construct(self):
        formula1 = MathTex(r"x + y = z")
        formula2 = MathTex(r"a + b = c")
        formula2.next_to(formula1, DOWN)
        self.play(Write(formula1), Write(formula2))
        self.wait()

class ScaleExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        formula.scale(2)
        self.play(Write(formula))
        self.wait()

class RotateExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        formula.rotate(PI/4)
        self.play(Write(formula))
        self.wait()

class GradientExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        formula.set_color_by_gradient(RED, BLUE)
        self.play(Write(formula))
        self.wait()

class OpacityExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        formula.set_opacity(0.5)
        self.play(Write(formula))
        self.wait()

class ShadowExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        shadow = formula.copy().set_color(GRAY).shift(DOWN * 0.1 + RIGHT * 0.1)
        self.play(Write(formula), Write(shadow))
        self.wait()

class StrokeExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        formula.set_stroke(width=2)
        self.play(Write(formula))
        self.wait()

class BackgroundExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        background = SurroundingRectangle(formula, color=YELLOW, fill_opacity=0.5)
        self.play(Create(background))
        self.play(Write(formula))
        self.wait()

class AnimateExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.shift(UP))
        self.wait()

class ColorChangeExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.set_color(RED))
        self.wait()

class OpacityChangeExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.set_opacity(0.5))
        self.wait()

class StrokeChangeExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.set_stroke(width=2))
        self.wait()

class AnimationGroupExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(AnimationGroup(
            formula.animate.shift(UP).set_color(RED),
            lag_ratio = 1
        ))
        self.wait()

class SuccessionExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(Succession(
            formula.animate.shift(UP).set_color(RED),
            lag_ratio = 1
        ))
        self.wait()

class WaitExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(Write(formula))
        self.wait(1)
        self.play(formula.animate.shift(UP))
        self.wait()

class RateFuncExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.shift(UP), rate_func=linear)
        self.wait(1)
        self.play(formula.animate.shift(DOWN), rate_func=smooth)
        self.wait()

class PathArcExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.shift(UP), path_arc=PI)
        self.wait()

class RunTimeExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.shift(UP), run_time=2)
        self.wait()

class LagRatioExample(Scene):
    def construct(self):
        formula = MathTex(r"x + y = z")
        self.play(formula.animate.shift(UP), lag_ratio=0.5)
        self.wait()