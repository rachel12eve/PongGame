from turtle import Turtle

FONT = "Courier"


class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)



