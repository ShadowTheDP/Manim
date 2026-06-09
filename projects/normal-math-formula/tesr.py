from manim import *

class SimpleTex(Scene):
    def construct(self):
        text = MathTex(r"\frac{4}{3} = 0.75")
        self.play(Write(text))
        self.wait(2)