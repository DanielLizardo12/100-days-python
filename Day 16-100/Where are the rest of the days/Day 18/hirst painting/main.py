import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("image.jpg", 50)
directions = [90, 180, 270, 0]

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.pensize(15)
timmy.speed(10)
y = -200
timmy.penup()
timmy.goto(-200, y)
for _ in range(10):

    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(colors).rgb)
        timmy.penup()
        timmy.forward(50)
    y += 50
    timmy.goto(-200, y)


screen.exitonclick()
