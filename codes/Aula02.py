from manim import *

class poligonos(Scene):
    def construct(self):

        poly3 = RegularPolygon(n = 3)
        poly3.set_fill(ORANGE, opacity = 0.5)
        poly3.set_stroke(WHITE, width = 3)
        poly3.scale(2)

        poly3_label = Text('Triângulo', font_size = 50)
        poly3_label.next_to(poly3, DOWN)

        self.play(Create(poly3))
        self.wait()
        self.play(Write(poly3_label))
        self.wait(3)

        
        poly4 = RegularPolygon(n = 4)
        poly4.set_fill(ORANGE, opacity = 0.5)
        poly4.set_stroke(WHITE, width = 4)
        poly4.scale(2)

        poly4_label = Text('Quadrado', font_size = 50)
        poly4_label.next_to(poly4, UP)

        self.play(ReplacementTransform(poly3, poly4), ReplacementTransform(poly3_label, poly4_label))
        self.wait(2)

        self.play(poly4.animate.rotate(PI/4), run_time = 2)
        self.wait()


        poly5 = RegularPolygon(n = 5)
        poly5.set_fill(GREEN, opacity = 0.5)
        poly5.set_stroke(WHITE, width = 4)
        poly5.scale(2)

        poly5_label = Text('Pentagono', font_size = 50)
        poly5_label.next_to(poly4, LEFT)

        self.play(ReplacementTransform(poly4, poly5), ReplacementTransform(poly4_label, poly5_label))
        self.wait(2)

        self.play(poly5.animate.shift(2*RIGHT))
        self.play(poly5_label.animate.shift(3*RIGHT+2*DOWN).scale(1.5))