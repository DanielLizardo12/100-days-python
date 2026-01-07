import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []


    def create_car(self):
        new_car = Turtle("square")
        new_car.shape()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        new_car.setposition(320, random.randint(-210, 210))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVING_DISTANCE)

