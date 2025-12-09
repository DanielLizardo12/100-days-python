from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(30)

def move_backwards():
    timmy.backward(30)

def counter_clockwise():
    timmy.left(30)

def clockwise():
    timmy.right(30)

def clear():
    timmy.home()
    timmy.clear()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()