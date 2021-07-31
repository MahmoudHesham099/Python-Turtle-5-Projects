from turtle import Screen
import time

from Ball import Ball
from Racket import Racket
from Scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Ping Pong')
screen.tracer(0)

right_racket = Racket((350, 0))
left_racket = Racket((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_racket.up, "Up")
screen.onkey(right_racket.down, "Down")
screen.onkey(left_racket.up, "w")
screen.onkey(left_racket.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)

    ball.move()

    # collision with racket
    if ball.distance(right_racket) < 50 and ball.xcor() > 320 or ball.distance(left_racket) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # right racket misses
    if ball.xcor() > 380:
        ball.goto_start()
        scoreboard.left_points()

    # left racket misses
    if ball.xcor() < -380:
        ball.goto_start()
        scoreboard.right_points()






screen.exitonclick()