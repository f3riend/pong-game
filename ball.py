from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.movement = [10,10]
        self.speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.movement[0],self.ycor() + self.movement[1])

    
    def boundX(self):
        self.movement[0] *= -1
        self.speed *= 0.9

    def bounceY(self):
        self.movement[1] *= -1

    
    def resetPostion(self):
        self.home()
        self.boundX()
        self.speed = 0.1
    