from turtle import Turtle, Screen
import heroes

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen")

for number in range(50):
    if number % 2 == 0:
        timmy.pendown()
    timmy.forward(10)
    timmy.penup()


screen = Screen()
screen.exitonclick()

print(heroes.gen())
