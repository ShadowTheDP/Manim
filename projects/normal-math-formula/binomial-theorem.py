from manim import *

class BinomialTheorem(Scene):
    def construct(self):
        # 二项式定理公式
        binomial_theorem = MathTex(
            "(a + b)^n = \\sum_{k=0}^{n} \\binom{n}{k} a^{n-k} b^k",
            font_size=40
        )

        # 显示公式
        self.play(Write(binomial_theorem))
        self.wait(2)

        # 展开公式
        expanded_form = MathTex(
            "(a + b)^n = \\binom{n}{0} a^n b^0 + \\binom{n}{1} a^{n-1} b^1 + \\cdots + \\binom{n}{n} a^0 b^n",
            font_size=40
        )

        # 替换为展开形式
        self.play(Transform(binomial_theorem, expanded_form))
        self.wait(2)

        # 结束
        self.play(FadeOut(binomial_theorem))