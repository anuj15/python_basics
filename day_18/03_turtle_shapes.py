import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape('turtle')
screen.colormode(255)


def get_turtle_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg


for i in range(3, 11):
    timmy.color(get_turtle_color())
    for j in range(i):
        direction = 360 / i
        timmy.forward(100)
        timmy.left(direction)

screen.exitonclick()
