from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
import random

COLORS = ['blue', 'red', 'aqua', 'green', 'pink', 'purple', 'white', 'orange']

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball1 = Ball()
score = Score()

screen.title("My Pong Game")

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball1.move_speed)
    ball1.move()

    # Detect Collision With Wall
    if ball1.ycor() > 280 or ball1.ycor() < -280:
        ball1.bounce_y()

    # Detect Collision with Right Paddle
    if ball1.distance(right_paddle) < 50 and ball1.xcor() > 320:
        ball1.bounce_x()
        right_paddle.color(random.choice(COLORS))

    # Detect Collision with Left Paddle
    if ball1.distance(left_paddle) < 50 and ball1.xcor() < -320:
        ball1.bounce_x()
        left_paddle.color(random.choice(COLORS))

        # Detect when the right paddle misses
    if ball1.xcor() > 380:
        ball1.reset_position()
        score.l_points()

    # Detect when the left paddle misses
    if ball1.xcor() < -380:
        ball1.reset_position()
        score.r_points()

screen.mainloop()
