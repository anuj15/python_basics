import turtle
from turtle import Screen, Turtle

import pandas

screen = Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
tim = Turtle()
tim.hideturtle()
tim.penup()
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
score = 0
guessed_states = []
remaining_states = [state for state in states]
for state in range(len(states)):
    answer = screen.textinput(title=f'Guess the State ({score}/50)', prompt='What\'s another state\'s name?').title()
    if answer == 'exit'.title():
        break
    if answer not in guessed_states:
        if answer in states:
            state_data = data[data.state == answer]
            tim.goto(x=state_data.x.item(), y=state_data.y.item())
            tim.write(arg=answer, move=False, align='center', font=('courier', 10, 'bold'))
            score += 1
            guessed_states.append(answer)
            remaining_states.remove(answer)
pandas.DataFrame(remaining_states).to_csv('remaining_states.csv')
