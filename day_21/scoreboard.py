from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'bold')


def read_high_score():
    with open('highest_score.txt') as f:
        contents = f.read()
    if contents == '':
        return 0
    else:
        return int(contents)


class Score(Turtle):

    def __init__(self):
        self.score = -1
        self.high_score = read_high_score()
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score:{self.score} High Score:{self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = -1
        self.update_score()
        self.write_high_score()

    def write_high_score(self):
        with open('highest_score.txt', 'w') as f:
            f.write(str(self.high_score))
