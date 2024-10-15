import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen for the Pong game
screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# Configure the screen settings
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)

# Set up key listeners for paddle movement
turtle.listen()
turtle.onkey(r_paddle.move_up, "Up")
turtle.onkey(r_paddle.move_down, "Down")
turtle.onkey(l_paddle.move_up, "w")
turtle.onkey(l_paddle.move_down, "s")

# Start the main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.time_sleep)  # Slow down the ball movement for smoother animation
    screen.update()
    ball.move()

    # Detect collision with the top or bottom of the screen and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with the paddles and bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    # Detect if the right paddle misses the ball
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    # Detect if the left paddle misses the ball
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

# Exit the game when the screen is clicked
screen.exitonclick()
