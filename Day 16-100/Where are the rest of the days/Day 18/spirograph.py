from turtle import Turtle, Screen
import random

def random_rgb():
    return random.randint(0, 255)

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.speed(0)
timmy.shape("circle")

number = 0.0
while number < 360:
    timmy.color((random_rgb(), random_rgb(), random_rgb()))
    timmy.circle(200)
    timmy.setheading(number)
    number += 0.1
screen.exitonclick()