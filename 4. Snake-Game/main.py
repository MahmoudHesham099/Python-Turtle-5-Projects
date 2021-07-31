from turtle import Screen
import time

from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # eat food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.generate()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    # collision with body
    for cube in snake.body_cubes:
        if cube == snake.head:
            pass
        elif snake.head.distance(cube) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()