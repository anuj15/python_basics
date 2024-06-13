import random
from turtle import Screen, Turtle

timmy = Turtle()
timmy.hideturtle()
timmy.speed(speed='fastest')
screen = Screen()
screen.colormode(255)


def get_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg


def draw_spirograph(size):
    for i in range(360 // size):
        timmy.color(get_color())
        timmy.setheading(i * size)
        timmy.circle(100)


draw_spirograph(5)
screen.exitonclick()
