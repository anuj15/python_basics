from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 30, 'bold')
COLOR = 'white'


class Score(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.score = -1
        self.color(COLOR)
        self.hideturtle()
        self.goto(x_position, 250)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, move=False, align=ALIGN, font=FONT)
