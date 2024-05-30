from common_methods import *


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def hurdle_1_2_3_4():
    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()
