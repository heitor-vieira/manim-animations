from manim import *

class Basic(Scene):  # Nome de classe geralmente começa com maiúscula
    def construct(self):
        quadrado = Square(side_length = 2)  # Corrigido "side_length"
        quadrado.set_fill(BLUE, opacity = 0.7)
        quadrado.move_to(2 * RIGHT + 1 * DOWN)

        self.play(Create(quadrado), run_time = 3)
        self.wait(2)

        circulo = Circle(radius = 3, color = WHITE)
        circulo.shift(3 * LEFT)
        circulo.set_fill(RED, opacity = 0.6)

        self.play(Create(circulo), run_time = 3)
        self.wait(2)

        triangulo = Triangle()

        self.play(Create(triangulo), run_time = 2)
        self.wait(2)

        triangulo2 = Triangle()
        triangulo2.set_fill(GREEN)
        triangulo2.move_to(3*RIGHT)

        self.play(FadeOut(circulo), FadeOut(quadrado))
        self.play(ReplacementTransform(triangulo, triangulo2))