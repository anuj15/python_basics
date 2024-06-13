from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-340, 270)
        self.level = -1
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(arg=f'Level: {self.level}', move=False, align='center', font=('Courier', 16, 'bold'))

    def game_over(self):
        self.home()
        self.write(arg='GAME OVER', move=False, align='center', font=('Courier', 20, 'bold'))
