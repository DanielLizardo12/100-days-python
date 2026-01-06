from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))

screen.listen()
screen.onkey(paddle1.go_up, "w")
screen.onkey(paddle1.go_down, "s")
screen.onkey(paddle2.go_up, "o")
screen.onkey(paddle2.go_down, "l")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()