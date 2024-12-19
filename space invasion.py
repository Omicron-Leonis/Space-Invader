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
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load('background.wav')
mixer.music.play(-1) # Loop the background music indefinitely

# Caption and Icon
pygame.display.set_caption("Sapce Invaader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
PLAYERx_CHANGE = 0

# Enemy
enemyImg = []
enemyX = []
enemyY= []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append (pygame.image.load(' enemy-png' ))
    enemyX. append (random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X) 
    enemyY_change.append (ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load( 'bullet.png' )
bullet = 0
bullety = playerY
bullet_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font( 'freesansbold.ttf', 32)
textx = 10
texty = 10

# Game Over Text
over_font = pygame.font.FONT('freesansbold.ttf', 64)

# FPS Control
clock = pygame.time.Clock()

def show_score(x, y):
    score = font.reader("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score,(x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (280,250))

def player(x, y):
    screen.blit(enemyImg[i], (x, y))