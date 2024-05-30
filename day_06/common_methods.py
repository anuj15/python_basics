def turn_left():
    print('turn left')


def move():
    print('move forward by 1 step')


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def object_here():
    print('check if object is present at current location or not')


def take(default=''):
    print(f'take object from current location {default}')


def put(default=''):
    print(f'put an object at current location {default}')


def wall_in_front():
    print('check if there is a wall in front or not')


def front_is_clear():
    print('check if there is a wall in front or not')


def wall_on_right():
    print('check if there is a wall on right or not')


def right_is_clear():
    print('check if there is a wall on right or not')


def at_goal():
    print('Check if goal is reached or not')


def build_wall():
    print('Build broken wall')
