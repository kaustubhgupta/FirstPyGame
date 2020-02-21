import pygame
import sys
import random
import time
pygame.init()
collisionVoice = pygame.mixer.Sound("collision_voice.wav")
movingVoice = pygame.mixer.Sound("moving_voice.wav")
pygame.mixer.music.load("bkg_Sound.wav")
pygame.mixer.music.play(-1)
# All Constant Variables
width = 800
height = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BackColor = (0, 0, 0)
playerSize = 50
playerPos = [width / 2, height - 2 * playerSize]
enemySize = 50
enemyPos = [random.randint(0, width - 1), 0]
enemyList = [enemyPos]
speed = 3
score = 0
gameOver = False
font = pygame.font.SysFont("monospace", 35)
# Screen Initialized
screen = pygame.display.set_mode((width, height))
# Setting Frame-rate
clock = pygame.time.Clock()
# Levels
def level(score, speed):
    if score < 10:
        speed = 4
    elif score < 30:
        speed = 8
    elif score < 50:
        speed = 13
    elif score < 90:
        speed = 17
    else:
        speed = 20
    return speed
# Dropping Blues
def drop(enemyList):
    delay = random.random()  # any value between 0 and 1
    if len(enemyList) < 10 and delay < 0.1:
        xi_pos = random.randint(0, width - enemySize)
        yi_pos = 0
        enemyList.append([xi_pos, yi_pos])
# Drawing Enemies
def drawEnemy(enemyList):
    for enemyPos in enemyList:
        pygame.draw.rect(screen, BLUE, (enemyPos[0], enemyPos[1], enemySize, enemySize))
# Update Enemy Position
def update(enemyList, score):
    for idx, enemyPos in enumerate(enemyList):
        if (enemyPos[1] >= 0) and (enemyPos[1] < height):  # Moving Blue Blocks
            enemyPos[1] += speed
        else:
            enemyList.pop(idx)
            score += 1
    return score
# Checking Collision
def checkCollision(enemyList, playerPos):
    for enemyPos in enemyList:
        if collision(playerPos, enemyPos):
            return True
    return False
# Detecting Collision
def collision(playerPos, enemyPos):
    p_x = playerPos[0]
    p_y = playerPos[1]
    e_x = enemyPos[0]
    e_y = enemyPos[1]
    if ((e_x >= p_x) and (e_x < p_x + playerSize)) or ((p_x >= e_x) and (p_x < e_x + playerSize)):
        if ((e_y >= p_y) and (e_y < p_y + playerSize)) or ((p_y >= e_y) and (p_y < e_y + playerSize)):
            return True
    else:
        return False
# Main Game Loop
while not gameOver:
    for event in pygame.event.get():  # Getting all types of events
        if event.type == pygame.QUIT:  # Handling exit control statements
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Moving Player Block
            x = playerPos[0]
            y = playerPos[1]
            if event.key == pygame.K_LEFT:
                x -= playerSize
                pygame.mixer.Sound.play(movingVoice)
            if event.key == pygame.K_RIGHT:
                x += playerSize
                pygame.mixer.Sound.play(movingVoice)
            if x == width or x == 0:
                x = 1
                pygame.mixer.Sound.play(movingVoice)
            playerPos = [x, y]
    screen.fill(BackColor)  # Set background after each move
    drop(enemyList)
    score = update(enemyList, score)
    speed = level(score, speed)
    text = "Score: " + str(score)
    label = font.render(text, 1, YELLOW)  # 1 for horizontal
    screen.blit(label, (width - 200, height - 400))
    if checkCollision(enemyList, playerPos):
        gameOver = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(collisionVoice)
        time.sleep(1)
        break
    drawEnemy(enemyList)
    pygame.draw.rect(screen, RED, (playerPos[0], playerPos[1], playerSize, playerSize))
    clock.tick(30)
    pygame.display.update()  # Renders objects on screen
# Hola, new features will be added soon!
def newFuntions():
    pass