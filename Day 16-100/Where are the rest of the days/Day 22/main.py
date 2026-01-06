from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up, "w")
screen.onkey(paddle1.go_down, "s")
screen.onkey(paddle2.go_up, "o")
screen.onkey(paddle2.go_down, "l")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle2) < 70 and ball.xcor() > 320 or ball.distance(paddle1) < 70 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()