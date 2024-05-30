from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
# screen.tracer(0)
screen.bgcolor('black')
screen.listen()

snake = Snake()
game_is_on = True

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

while game_is_on:
    snake.move_snake()

screen.exitonclick()
