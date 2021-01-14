from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_move = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_turn(self):
        self.y_move *= -1

    def x_turn(self):
        self.x_move *= -1
        self.speed_move *= 0.9

    def reset_game(self):
        self.home()
        self.speed_move = 0.1
        self.x_turn()
        self.y_turn()
