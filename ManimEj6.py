from manim import *
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(RED, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(GREEN, opacity=0.5)  # set the color and transparency

        square.next_to(circle, UP, buff=0.5)  # set the position
        #square.next_to(circle, DOWN, buff=0.5)  # set the position
        #square.next_to(circle, LEFT, buff=0.5)  # set the position
        #square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen