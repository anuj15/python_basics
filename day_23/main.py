import random
import time
from turtle import Screen

from cars import CarManager
from levels import Level
from timmy import Tim

screen = Screen()
screen.tracer(0)

count = random.randint(5, 10)
car = CarManager()
level = Level()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Turtle Crossing Game')
turtle = Tim()
screen.onkey(key='Up', fun=turtle.move_up)
screen.onkey(key='Down', fun=turtle.move_down)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move()
    if turtle.ycor() >= 280:
        turtle.restart()
        level.level_up()
        car.increase_cars()
        car.increase_speed()
    for cars in car.car_manager:
        if turtle.distance(cars) < 30:
            level.game_over()
            game_is_on = False

screen.exitonclick()
