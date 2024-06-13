import random
from turtle import Turtle, Screen

screen = Screen()
turtles = []
y = -200
is_race_on = True
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
my_choice = screen.textinput(title='Turtle Race', prompt='Which turtle will win the race? Enter a color: ').lower()
for color in colors:
    timmy = Turtle(shape='turtle')
    timmy.color(color)
    timmy.penup()
    y += 50
    timmy.goto(x=-230, y=y)
    turtles.append(timmy)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.color()[0]
            if my_choice == winner:
                print(f'You won! The winner is: {winner}')
            else:
                print(f'You lose! The winner is: {winner}')
        turtle.speed(random.randint(1, 10))
        turtle.forward(random.randint(1, 10))

screen.exitonclick()
