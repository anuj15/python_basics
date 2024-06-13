import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.shape('turtle')

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen.exitonclick()
