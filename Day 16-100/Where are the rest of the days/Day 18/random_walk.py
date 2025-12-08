from turtle import Turtle, Screen
import random

directions = [90, 180, 270, 0]

def random_rgb():
    return random.randint(1, 255)

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.pensize(10)
timmy.speed(6)

for _ in range(100):
    timmy.color((random_rgb(), random_rgb(), random_rgb()))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))



screen.exitonclick()