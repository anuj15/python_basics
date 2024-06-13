from turtle import Turtle


class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.restart()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.back(10)

    def restart(self):
        self.goto(0, -280)
        self.setheading(90)
