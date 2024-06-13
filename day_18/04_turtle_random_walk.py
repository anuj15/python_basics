import random
from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()
timmy.hideturtle()
timmy.speed(speed='fastest')
timmy.pensize(width=10)
screen.colormode(255)
directions = [0, 1, 2, 3]


def get_turtle_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg


for i in range(200):
    timmy.color(get_turtle_color())
    timmy.forward(20)
    direction = 90 * random.choice(directions)
    timmy.setheading(direction)

screen.exitonclick()
