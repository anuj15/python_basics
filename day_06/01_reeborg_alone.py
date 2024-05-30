from common_methods import *


def draw_left_square():
    move()
    for i in range(3):
        turn_left()
        move()


def draw_right_square():
    turn_left()
    for i in range(3):
        move()
        turn_right()
    move()
