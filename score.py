from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1 = 0
        self.player2 = 0

        self.update()
        self.line()
        
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.player1,align="center",font=("Courier",40,"normal"))
        self.goto(100,200)
        self.write(self.player2,align="center",font=("Courier",40,"normal"))
    
    def line(self):
        brush = Turtle()
        brush.color("white")
        brush.setheading(90)
        brush.penup()
        brush.hideturtle()
        brush.goto(0,-300)
        for i in range(60):
            brush.up()
            brush.forward(10)
            brush.down()
            brush.forward(10)