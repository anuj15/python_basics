from common_methods import *


def around_1():
    for i in range(4):
        for j in range(9):
            move()
        turn_left()


def around_1_variable():
    put()
    if wall_in_front():
        turn_left()
        move()
    else:
        move()
    while not object_here():
        move()
        if wall_in_front():
            turn_left()


def around_1_apple():
    for i in range(40):
        if object_here():
            take()
        if not wall_in_front():
            move()
        else:
            turn_left()


def around_2_3_4():
    put()
    if wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
            move()
    else:
        move()
    while not object_here():
        if wall_in_front():
            turn_left()
        elif wall_on_right():
            move()
        else:
            turn_right()
            move()
