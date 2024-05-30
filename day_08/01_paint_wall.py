# Given: 1 can of paint can cover 5 square meters of wall
# Number of cans = height * width + coverage per can
import math


def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / cover)
    print(f'You\'ll need {cans} cans of paint.')


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
