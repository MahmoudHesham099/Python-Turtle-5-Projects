import random
import turtle
from turtle import Turtle, Screen

theTurtle = Turtle()
theTurtle.shape('turtle')
theTurtle.penup()
theTurtle.setx(-220)
theTurtle.sety(-150)
theTurtle.pensize(5)
theTurtle.pendown()
theTurtle.speed('fastest')
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(sides):
    angle = 360 / sides
    theTurtle.color(random_color())
    for _ in range(sides):
        theTurtle.forward(100)
        theTurtle.left(angle)


def draw_spirograph():
    for _ in range(36):
        theTurtle.color(random_color())
        theTurtle.circle(70)
        theTurtle.setheading(theTurtle.heading() + 10)


for shape in range(3, 12):
    draw_shape(shape)

theTurtle.penup()
theTurtle.setx(200)
theTurtle.sety(0)
theTurtle.pensize(1)
theTurtle.pendown()

draw_spirograph()

theScreen = Screen()
theScreen.exitonclick()
