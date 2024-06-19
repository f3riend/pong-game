from turtle import Screen,Turtle
from player import Player
from ball import Ball
from score import Score
from time import sleep

canvas = Screen()
canvas.setup(width=800,height=600)
canvas.bgcolor("black")
canvas.title("Pong Game")
canvas.tracer(0) #Animasyonları otomatikleştirmeyi kapatıyoruz

player1 = Player((-350,0))
player2 = Player((350,0))
ball = Ball()

score = Score()

canvas.listen()

#player1 movements
canvas.onkey(player1.up,"w")
canvas.onkey(player1.down,"s")

#player2 movements
canvas.onkey(player2.up,"Up")
canvas.onkey(player2.down,"Down")



isGameOn = True
while isGameOn:
    sleep(ball.speed)
    canvas.update() #Animasyonları manuel olarak güncelliyoruz
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    
    if ball.distance(player1) < 50 and ball.xcor() < -320 or ball.distance(player2) < 50 and ball.xcor() > 320:
        ball.boundX()
        #distance methodu 2 nesne arasındaki mesafeyi 2 nesnenin ortasından ihtibaren ölçmeye başlar
        #dolayısıyla player boyutu width 20 height 100 olduğu için 50 kullanıyoruz
    
    if ball.xcor() > 380:
            ball.resetPostion()
            score.player1+= 1
            score.update()
    
    if ball.xcor() < -380:
        ball.resetPostion()
        score.player2+= 1
        score.update()
    
    
canvas.exitonclick()