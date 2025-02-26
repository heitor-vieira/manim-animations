from manim import * 

class poligonos(Scene): 
    def construct(self):

        poly3 = RegularPolygon(n=3)
        poly3.set_fill(ORANGE, opacity = 0.5)
        poly3.set_stroke(WHITE, width = 3)
        poly3.scale(2)

        poly3_label = Text('Triangulo', font_size = 50)
        poly3_label.next_to(poly3, DOWN)

        self.play(Create(poly3))
        self.wait()
        self.play(Write(poly3_label))
        self.wait(3)

        poly4 = RegularPolygon(n=4)
        poly4.set_fill(BLUE, opacity = 0.5)
        poly4.set_stroke(WHITE, width = 4)
        poly4.scale(2)

        poly4_label = Text('Quadrado', font_size = 60)
        poly4_label.next_to(poly4, UP)

        self.play(ReplacementTransform(poly3, poly4), ReplacementTransform(poly3_label, poly4_label))
        self.wait(2)

        self.play(poly4.animate.rotate(PI/4), run_time = 2)
        self.wait()

        poly5 = RegularPolygon(n=5)
        poly5.set_fill(GREEN, opacity = 0.5)
        poly5.set_stroke(WHITE, width = 4)
        poly5.scale(2)

        poly5_label = Text('Pentagono', font_size = 30)
        poly5_label.next_to(poly5, LEFT)

        self.play(ReplacementTransform(poly4, poly5), ReplacementTransform(poly4_label, poly5_label))

        self.play(poly5.animate.shift(2*RIGHT))
        self.play(poly5_label.animate.shift(3*RIGHT+2*DOWN).scale(1.5))

class animapoly(Scene):
    def construct(self):

        circle = Circle()
        circle.set_fill(BLUE, opacity = 0.8)
        circle.set_stroke(WHITE, width = 5)
        circle.scale(2)

        poly3 = RegularPolygon(n=3)
        poly3.set_fill(YELLOW, opacity = 0.7)
        poly3.set_stroke(WHITE, width = 3)
        poly3.scale(2)
        poly3.shift(0.2*UP)

        poly4 = RegularPolygon(n=4)
        poly4.set_fill(YELLOW, opacity = 0.7)
        poly4.set_stroke(WHITE, width = 3)
        poly4.scale(2)

        poly5 = RegularPolygon(n=5)
        poly5.set_fill(YELLOW, opacity = 0.7)
        poly5.set_stroke(WHITE, width = 3)
        poly5.scale(2)

        poly6 = RegularPolygon(n=6)
        poly6.set_fill(YELLOW, opacity = 0.7)
        poly6.set_stroke(WHITE, width = 3)
        poly6.scale(2)

        poly7 = RegularPolygon(n=7)
        poly7.set_fill(YELLOW, opacity = 0.7)
        poly7.set_stroke(WHITE, width = 3)
        poly7.scale(2)

        poly8 = RegularPolygon(n=8)
        poly8.set_fill(YELLOW, opacity = 0.7)
        poly8.set_stroke(WHITE, width = 3)
        poly8.scale(2)

        poly9 = RegularPolygon(n=9)
        poly9.set_fill(YELLOW, opacity = 0.7)
        poly9.set_stroke(WHITE, width = 3)
        poly9.scale(2)

        poly10 = RegularPolygon(n=10)
        poly10.set_fill(YELLOW, opacity = 0.7)
        poly10.set_stroke(WHITE, width = 3)
        poly10.scale(2)

        poly11 = RegularPolygon(n=11)
        poly11.set_fill(YELLOW, opacity = 0.7)
        poly11.set_stroke(WHITE, width = 3)
        poly11.scale(2)

        poly12 = RegularPolygon(n=12)
        poly12.set_fill(YELLOW, opacity = 0.7)
        poly12.set_stroke(WHITE, width = 3)
        poly12.scale(2)

        self.play(Create(circle))
        self.wait(2)

        self.play(Create(poly3))
        self.wait(2)

        self.play(ReplacementTransform(poly3, poly4), run_time = 1.6)
        self.play(ReplacementTransform(poly4, poly5), run_time = 1.4)
        self.play(ReplacementTransform(poly5, poly6), run_time = 1.2)
        self.play(ReplacementTransform(poly6, poly7), run_time = 1.0)
        self.play(ReplacementTransform(poly7, poly8), run_time = 0.8)
        self.play(ReplacementTransform(poly8, poly9), run_time = 0.6)
        self.play(ReplacementTransform(poly9, poly10), run_time = 0.6)
        self.play(ReplacementTransform(poly10, poly11), run_time = 0.6)
        self.play(ReplacementTransform(poly11, poly12), run_time = 0.6)

        self.wait(3)