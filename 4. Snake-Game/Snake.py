from turtle import Turtle

STARTING_SNAKE_CUBES_POSITION = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body_cubes = []
        for pos in STARTING_SNAKE_CUBES_POSITION:
            self.create_cube(pos)
        self.head = self.body_cubes[0]

    def create_cube(self, position):
        new_cube = Turtle('square')
        new_cube.color('green')
        new_cube.penup()
        new_cube.goto(position)
        self.body_cubes.append(new_cube)

    def move(self):
        for cube_num in range(len(self.body_cubes) - 1, 0, -1):
            new_x = self.body_cubes[cube_num - 1].xcor()
            new_y = self.body_cubes[cube_num - 1].ycor()
            self.body_cubes[cube_num].goto(new_x, new_y)
        self.head.forward(20)

    def extend(self):
        self.create_cube(self.body_cubes[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)