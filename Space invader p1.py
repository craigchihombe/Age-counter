import math
import random
import pygame

#Constant
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMEY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()
#Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#Caption and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load("UFO.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

#Creating enemies
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMEY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)