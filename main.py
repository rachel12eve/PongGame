# TODO 1a.create the screen
# TODO 1. create a line in the middle
# TODO 2. create 2 scores
# TODO 3. create 2 paddle that can move up and down
# TODO 4. create the ball
# TODO 5. when it hit the pong, it move the move, but how?
# TODO 6. create the "wall" when it hits, game over

from turtle import Screen
import time

from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

game_is_on = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

r_scoreboard = Scoreboard((100, 180))
l_scoreboard = Scoreboard((-100, 180))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(ball.speed_move)

    screen.update()  # show after all three moved
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_turn()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_turn()

    # detect paddle miss
    if ball.xcor() > 380:
        ball.reset_game()
        l_scoreboard.add_lscore()

    if ball.xcor() < -380:
        ball.reset_game()
        r_scoreboard.add_rscore()

screen.exitonclick()
