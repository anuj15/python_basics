import random
from turtle import Turtle

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


class CarManager:
    def __init__(self):
        self.car_manager = []
        self.car_count = 5
        self.car_speed = 10

    def create_car(self):
        if random.randint(1, 6) == 6:
            new_car = Turtle()
            new_car.color(random.choice(colors))
            new_car.shape('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.penup()
            y = random.randint(-250, 250)
            new_car.goto(360, y)
            self.car_manager.append(new_car)

    def increase_cars(self):
        for car in range(self.car_count):
            self.create_car()
        self.car_count += 5

    def increase_speed(self):
        self.car_speed += 5

    def move(self):
        for car in self.car_manager:
            car.forward(self.car_speed)
