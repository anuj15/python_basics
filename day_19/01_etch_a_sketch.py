from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.back(10)


def turn_left():
    timmy.left(10)


def turn_right():
    timmy.right(10)


def clear_all():
    timmy.clear()
    timmy.reset()


screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_all)

screen.exitonclick()
