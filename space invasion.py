import math
import pygame
import random
from pygame import mixer

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)  # Loop the background music indefinitely

# Caption and Icon
pygame.display.set_caption("Sapce Invaader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
PLAYERX_CHANGE = 0

# Enemy
enemyImg = []
enemyX = []
enemyY= []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append (pygame.image.load('enemy.png'))
    enemyX. append (random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X) 
    enemyY_change.append (ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load('bullet.png' )
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# FPS Control
clock = pygame.time.Clock()

def show_score(x, y):
    score = font.reader("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score,(x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200,250))

def player(x, y):
    screen.blit(enemyImg[i], (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
  global bullet_state
  bullet_state = "fire"
  screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(obj1X, obj1Y, obj2X, obj2Y, distance_threshold):
    distance = math. sqrt(math.pow(obj1X - obj2X, 2) + math. pow(obj1Y - obj2Y, 2))
    return distance < distance_threshold

# Game Loop
running = True
game_over_flag = False

while running:
    screen.fill((0,0,0))
    screen. blit(background, (0, 0))
    for event in pygame.event.get():
        if event. type == pygame. QUIT:
           running = False
        
        if event.type == pygame.KEYDOWN and not game_over_flag:
            if event.key == pygame. K_LEFT:
               playerX_change = -2

            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame. K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound .play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    if game_over_flag:
        # Stop the background music when the game is over
        mixer.music.stop()
        game_over_text()
        pygame.display.update()
        continue

    # Player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64)) # Ensure player stays within screen

    # Enemy Movement
    for i in range(num_of_enemies):
        # Game Over Condition: Enemy touches player
        if isCollision (enemyX[i], enemyY[i], playerX, playerY, COLLISION_DISTANCE + 20):
           for j in range(num_of_enemies) :
               enemyY[j] = 2000 # Move all enemies off-screen    
           game_over_flag = True
           break

        enemyX[i] += enemyX_change[ i]
        if enemyX[i] < 0 or enemyX[i] >= SCREEN_WIDTH - 64:
           enemyX_change [i] *= -1
           enemyY [i] += enemyY_change[i]
        
        #Collision Bullet hits enemy
        collision = isCollision(enemyX[i], enemyY[i], bullet, bulletY, COLLISION_DISTANCE)
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint( ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyX[i], enemyY[i], i)
    # Bullet Movement
    if bulletY <= 0:
       bulletY = playerY
       bullet_state = "ready"
    if bullet_state == "fire":
       fire_bullet(bulletX, bulletY)
       bulletY -= bulletY_change

    player (player, playerY) 
    show_score(textx, texty) 
    pygame.display.update()
    # Cap the frame rate
    clock. tick(60)









