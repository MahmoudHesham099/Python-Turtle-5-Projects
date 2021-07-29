from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Choose a car", prompt="Red, Green OR Yellow?")
cars = ["Red", "Green", "Yellow"]
vertical_positions = [-70, 0, 70]
created_cars = []

# Create cars
for car in cars:
    car_shape = f"gifs/{car}.gif"
    screen.addshape(car_shape)
    new_car = Turtle(shape=car_shape)
    new_car.penup()
    new_car.goto(x=-200, y=vertical_positions[cars.index(car)])
    created_cars.append(new_car)

# Begin the race after choose a car
if user_choice:
    race_on = True

while race_on:
    for running_car in created_cars:
        if running_car.xcor() > 210:
            race_on = False
            winning_car = running_car.shape()
            winning_car_color = winning_car[5:-4] # gifs/red.gif => red
            if winning_car_color.lower() == user_choice.lower():
                print(f"You Win! The {winning_car_color} car is the winner!")
            else:
                print(f"You Lose! The {winning_car_color} car is the winner!")

        # move cars forward by random integer
        rand_dis = random.randint(1, 10)
        running_car.forward(rand_dis)

screen.exitonclick()
