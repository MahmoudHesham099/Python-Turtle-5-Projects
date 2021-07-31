from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color('red')
        self.speed('fastest')
        self.penup()
        self.generate()

    def generate(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 260)
        self.goto(rand_x, rand_y)
