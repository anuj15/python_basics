from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
screen = Screen()
for _ in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen.exitonclick()
