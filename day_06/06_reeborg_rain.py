from common_methods import *


def rain_0():
    for i in range(6):
        move()
    build_wall()
    turn_around()
    for i in range(5):
        move()


def rain_1():
    move()
    turn_right()
    move()

    while not at_goal():
        if front_is_clear():
            if wall_on_right():
                move()
            else:
                turn_right()
                build_wall()
                turn_left()
        else:
            turn_left()
