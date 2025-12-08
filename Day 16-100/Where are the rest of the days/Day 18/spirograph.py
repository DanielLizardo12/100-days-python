import turtle
from turtle import Turtle, Screen
import random

def random_rgb():
    return random.randint(0, 255)

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.speed(0)
timmy.shape("circle")


for number in range(360):
    timmy.color((random_rgb(), random_rgb(), random_rgb()))
    timmy.circle(200)
    timmy.setheading(number)



screen.exitonclick()