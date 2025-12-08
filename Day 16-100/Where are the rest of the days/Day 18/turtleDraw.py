from turtle import Turtle, Screen
import random

def random_rgb():
    return random.randint(1, 255)

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen")

for number in range(4, 10):
    timmy.pencolor((random_rgb(), random_rgb(), random_rgb()))
    for _ in range(number):
        timmy.forward(100)
        timmy.right(360 / number)



screen.exitonclick()