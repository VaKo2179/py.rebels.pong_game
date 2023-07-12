from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
paddle = Paddle((350, 0))
paddle1 = Paddle((-350, 0))
ball = Ball()
scoreboard=Scoreboard()

screen.setup(800, 600)
screen.bgcolor("black")
screen.listen()
screen.onkey(paddle.move_down, "Down")
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle1.move_up, "w")
screen.title("pong")

game_on = True

while game_on:
    ball.move()
    time.sleep(0.005)  # Adjust the sleep time for smoother movement
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        screen.update()

    if ball.distance(paddle) < 40 and ball.xcor() > 320 or ball.distance(paddle1) < 40 and ball.xcor() < 320:
        ball.bounce_x()

    if ball.xcor() > 450:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -450:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
