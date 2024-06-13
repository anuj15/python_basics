import time
from turtle import Screen

from food import Food
from scoreboard import Score
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Snake Game')
screen.bgcolor('black')
screen.listen()

snake = Snake()
food = Food()
score = Score()

game_is_on = True

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 20:
        score.update_score()
        food.update_location()
        snake.extend()
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 300:
        score.reset()
        snake.reset()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 15:
            score.reset()
            snake.reset()

screen.exitonclick()
