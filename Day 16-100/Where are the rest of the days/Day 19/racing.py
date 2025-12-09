import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? enter a color: ")

colors = ["purple", "blue", "green", "yellow", "orange", "red", "brown"]
turtles = []

def set_turtles(i, y):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.setposition(-200, y)
    return turtle

position = -150
for number in range(7):
    turtles.append(set_turtles(number, position))
    position += 50

race_finished = False
while not race_finished:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_finished = True
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! {winning_color} turtle is the winner")
            else:
                print(f"you lose! {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()