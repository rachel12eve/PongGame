# TODO 1a.create the screen
# TODO 1. create a line in the middle
# TODO 2. create 2 scores
# TODO 3. create 2 paddle that can move up and down
# TODO 4. create the ball
# TODO 5. when it hit the pong, it move the move, but how?
# TODO 6. create the "wall" when it hits, game over

from turtle import Turtle, Screen, penup
import time

from paddle import Paddle

game_is_on = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    screen.update()  # show after all three moved
    time.sleep(0.1)

screen.exitonclick()
