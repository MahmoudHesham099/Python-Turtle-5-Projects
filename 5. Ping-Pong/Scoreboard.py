from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 220)
        self.write(self.right_score, align="center", font=('Courier', 60, 'normal'))
        self.goto(-100, 220)
        self.write(self.left_score, align="center", font=('Courier', 60, 'normal'))

    def right_points(self):
        self.right_score += 1
        self.update_score()

    def left_points(self):
        self.left_score += 1
        self.update_score()
