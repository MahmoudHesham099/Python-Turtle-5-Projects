from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y_COR = 280


class Player(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        turtle_shape = f"gifs/new_turtle.gif"
        self.screen.addshape(turtle_shape)
        self.shape(turtle_shape)
        self.penup()
        self.goto_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def reach_finish_line(self):
        if self.ycor() > FINISH_LINE_Y_COR:
            return True
        else:
            return False
