import time
from turtle import Screen

from ball import Ball
from net import Net
from paddles import Paddle
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.listen()
net = Net()
left_score = Score(x_position=-50)
right_score = Score(x_position=50)
l_paddle = Paddle(x_paddle=-380)
r_paddle = Paddle(x_paddle=380)
ball = Ball()
sleep_time = 0.1
game_is_on = True
screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.onkey(key='a', fun=l_paddle.up)
screen.onkey(key='z', fun=l_paddle.down)

while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move()
    # PADDLE HIT
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -340) or (ball.distance(r_paddle) < 50 and ball.xcor() > 340):
        ball.bounce_x()
        sleep_time *= 0.9
    # RIGHT MISS
    elif ball.xcor() > 390:
        ball.reset_position()
        left_score.update_score()
    # LEFT MISS
    elif ball.xcor() < -390:
        ball.reset_position()
        right_score.update_score()
    # UPPER OR LOWER WALL HIT
    elif abs(ball.ycor()) > 280:
        ball.bounce_y()

screen.exitonclick()
