from sys import exit
import pygame, random, os
pygame.init()
pygame.font.init()
pygame.mixer.init()  

width = 600
height = 338
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Modern Pong Game")
backgroundColor = pygame.Color(0, 0, 0)
separatorColor = pygame.Color(13, 13, 13)
whiteColor = pygame.Color(255, 255, 255)
scoreColor = pygame.Color(255, 236, 220)
paddleColor = pygame.Color(255, 255, 255)
ballColor = pygame.Color(154,19,19) 


current = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current, "assets", "Knewave-Regular.ttf")
knewave = pygame.font.Font(path, 24)


paddleSoundPath = os.path.join(current, "assets", "paddle_hit.wav")
wallSoundPath = os.path.join(current, "assets", "wall_effect.mp3")

try:
    paddleHitSound = pygame.mixer.Sound(paddleSoundPath)
except:
    print("Paddle hit sound file could not be loaded! Check the path of the sound file.")
    paddleHitSound = None

try:
    wallHitSound = pygame.mixer.Sound(wallSoundPath)
except:
    print("Wall hit sound file could not be loaded! Check the path of the sound file.")
    wallHitSound = None


player1Score = player2Score = 0


paddleWidth = 10
paddleHeight = 60
paddleSpeed = 5


player1X = 20
player1Y = height // 2 - paddleHeight // 2
player1Rect = pygame.Rect(player1X, player1Y, paddleWidth, paddleHeight)


player2X = width - 20 - paddleWidth
player2Y = height // 2 - paddleHeight // 2
player2Rect = pygame.Rect(player2X, player2Y, paddleWidth, paddleHeight)


ballSize = 18  
ballX = width // 2 - ballSize // 2
ballY = height // 2 - ballSize // 2
ballSpeedX = 4 * random.choice((1, -1))  
ballSpeedY = 4 * random.choice((1, -1))
ballRect = pygame.Rect(ballX, ballY, ballSize, ballSize)


scoreboardText = knewave.render("Score", True, scoreColor)
player1ScoreText = knewave.render(f"{player1Score}", True, scoreColor)
player2ScoreText = knewave.render(f"{player2Score}", True, scoreColor)
separator = pygame.Surface((3, 338))
separator.fill(separatorColor)


clock = pygame.time.Clock()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_w] and player1Y > 0:  
        player1Y -= paddleSpeed
    if keys[pygame.K_s] and player1Y < height - paddleHeight:  
        player1Y += paddleSpeed
    
    
    if keys[pygame.K_UP] and player2Y > 0:  
        player2Y -= paddleSpeed
    if keys[pygame.K_DOWN] and player2Y < height - paddleHeight:  
        player2Y += paddleSpeed
    
    
    ballX += ballSpeedX
    ballY += ballSpeedY
    
    
    if ballY <= 0 or ballY >= height - ballSize:
        ballSpeedY *= -1
        
        if wallHitSound:
            wallHitSound.play()
    
    
    ballRect.x = ballX
    ballRect.y = ballY
    
    if ballRect.colliderect(player1Rect) or ballRect.colliderect(player2Rect):
        ballSpeedX *= -1
        
        if paddleHitSound:
            paddleHitSound.play()
    
    
    if ballX <= 0:
        player2Score += 1
        player2ScoreText = knewave.render(f"{player2Score}", True, scoreColor)
        
        ballX = width // 2 - ballSize // 2
        ballY = height // 2 - ballSize // 2
        ballSpeedX = abs(ballSpeedX)  
        ballSpeedY = 4 * random.choice((1, -1))
    
    if ballX >= width - ballSize:
        player1Score += 1
        player1ScoreText = knewave.render(f"{player1Score}", True, scoreColor)
        
        ballX = width // 2 - ballSize // 2
        ballY = height // 2 - ballSize // 2
        ballSpeedX = -abs(ballSpeedX)  
        ballSpeedY = 4 * random.choice((1, -1))
    
    
    player1Rect.y = player1Y
    player2Rect.y = player2Y
    
    
    window.fill(backgroundColor)
    
    
    window.blit(separator, (width // 2 - 1, 0))
    
    
    window.blit(scoreboardText, (262, 39))
    window.blit(player1ScoreText, (142, 286))
    window.blit(player2ScoreText, (442, 286))
    
    
    pygame.draw.rect(window, paddleColor, player1Rect)
    pygame.draw.rect(window, paddleColor, player2Rect)
    
    
    pygame.draw.ellipse(window, ballColor, ballRect)
    
    
    pygame.display.flip()
    clock.tick(60)