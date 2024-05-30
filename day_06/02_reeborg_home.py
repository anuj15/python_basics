from common_methods import *


def make_l():
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()


def next_l():
    turn_right()
    move()
    turn_right()


def home_1():
    move()
    move()


def home_2():
    move()
    move()


def home_3():
    move()
    move()
    turn_left()
    move()


def home_4():
    make_l()
    for i in range(3):
        next_l()
        make_l()
