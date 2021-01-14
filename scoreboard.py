from turtle import Turtle

FONT = "Courier"


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.goto(position)
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))

    def add_rscore(self):
        self.clear()
        self.r_score += 1
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    def add_lscore(self):
        self.clear()
        self.l_score += 1
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))

