from turtle import Turtle

FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 240)
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f" level {self.level}", font=("Arial", 30, "bold"))

    def reset_level(self):
        self.level = 0
        self.update_level()
