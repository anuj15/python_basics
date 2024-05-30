from common_methods import *


def up_one_step():
    turn_left()
    move()
    turn_right()
    move()
    move()


def down_one_step():
    turn_around()
    move()
    move()
    turn_left()
    move()
    turn_left()


def newspaper_0_1():
    take('star')

    for i in range(3):
        up_one_step()

    while object_here():
        take('token')

    put('star')

    for i in range(3):
        down_one_step()
