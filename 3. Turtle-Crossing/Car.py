from turtle import Turtle
import random

cars = ['Red', 'Green', 'Yellow']
INITIAL_SPEED = 5
INCREMENT_SPEED = 10


class Car:

    def __init__(self, screen):
        self.screen = screen
        self.all_cars = []
        self.car_speed = INITIAL_SPEED
        for car in cars:  # Add cars shapes
            car_shape = f"gifs/{car}.gif"
            self.screen.addshape(car_shape)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_index = random.randint(0, 2)
            random_car = cars[random_index]
            created_car = Turtle(shape=f"gifs/{random_car}.gif")
            created_car.penup()
            random_y = random.randint(-250, 250)
            created_car.goto(-300,random_y)
            self.all_cars.append(created_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT_SPEED
