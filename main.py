from turtle import Turtle, Screen

jim = Turtle()
jim.shape("turtle")


def move_forwards():
    jim.fd(10)


def move_backwards():
    jim.bk(10)


def turn_left():
    new_heading = jim.heading() + 10
    jim.setheading(new_heading)


def turn_right():
    new_heading = jim.heading() - 10
    jim.setheading(new_heading)


def clear():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


screen = Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
