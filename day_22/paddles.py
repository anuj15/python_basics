from turtle import Turtle

COLOR = 'white'
SHAPE = 'square'
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x_paddle):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_paddle, 0)

    def up(self):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
