from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        # Move the paddle up by 20 pixels
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        # Move the paddle down by 20 pixels
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)