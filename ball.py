from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.time_sleep = 0.1

    def move(self):
        # Move the ball by updating its position in both x and y directions
        self.goto(self.xcor() + self.x_move,self.ycor() + self.y_move)

    def bounce_y(self):
        # Reverse the y-direction to simulate bouncing off the top/bottom wall
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the x-direction to simulate bouncing off a paddle and speed up the ball
        self.x_move *= -1
        self.time_sleep *= 0.9  # Increase ball speed by decreasing sleep time

    def refresh(self):
        # Reset the ball to the center and reset its speed
        self.goto(0, 0)
        self.time_sleep = 0.1
        self.bounce_x()  # Send the ball towards the opponent's side