from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.penup()
        self.right(90)
        self.goto(0, -375)
        self.step = 20

    def home(self):
        self.goto(0, -375)

    def move_right(self):
        self.goto(self.xcor()+self.step, self.ycor())

    def move_left(self):
        self.goto(self.xcor()-self.step, self.ycor())

