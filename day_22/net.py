from turtle import Turtle

COLOR = 'white'


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.width(5)
        self.color(COLOR)
        self.goto(0, -300)
        self.setheading(90)
        for i in range(150):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
