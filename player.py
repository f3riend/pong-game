from turtle import Turtle


class Player(Turtle):

    def __init__(self,position):
        super().__init__()
        self.MOVEMENT = 20
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(),self.ycor() + self.MOVEMENT)

    def down(self):
        self.goto(self.xcor(),self.ycor() - self.MOVEMENT)