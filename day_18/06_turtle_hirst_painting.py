import random
from turtle import Turtle, Screen
import turtle

import colorgram

colors = colorgram.extract(f='hirst_painting.jpg', number_of_colors=25)
color_list = [(x.rgb.r, x.rgb.g, x.rgb.b) for x in colors]

timmy = Turtle()
turtle.colormode(255)
screen = Screen()
timmy.speed(speed='fastest')
timmy.hideturtle()
timmy.pensize(width=20)
timmy.penup()
x = timmy.xcor() - 250
y = timmy.ycor() - 250

for i in range(10):
    timmy.setpos(x, y + 40 * i)
    for _ in range(25):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(30)

screen.exitonclick()
