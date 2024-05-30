from turtle import Turtle

SEGMENTS_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for seg in range(len(SEGMENTS_POSITIONS)):
            new_segment = Turtle(shape='square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.setpos(SEGMENTS_POSITIONS[seg])
            self.segments.append(new_segment)

    def move_snake(self):
        for seg in range(len(SEGMENTS_POSITIONS) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].setpos(new_x, new_y)
        self.head.forward(SNAKE_STEPS)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
