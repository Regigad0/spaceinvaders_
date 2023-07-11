"""
    this is a game with "space invader" theme

"""
import random
import pygame
import math
# Initialized pygame
pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 600))

# set icon and title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("obvni.png")
pygame.display.set_icon(icon)
background = pygame.image.load("pexels-philippe-donn-1257860.jpg")

# Player Variables
img_player = pygame.image.load("1455554775_line-85_icon-icons.com_53362.png")
player_x = 368
player_y = 538
player_x_change = 0
player_y_change = 0

#enemy variables
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 5

for i in range(number_of_enemies):
    img_enemy.append(pygame.image.load("Martian_icon-icons.com_54167.png"))
    enemy_x.append(random.randint(0, 768))
    enemy_y.append(random.randint(30, 200))
    enemy_x_change.append(0.6)
    enemy_y_change.append(30)


def player(x, y):
    screen.blit(img_player, (x, y))

#show enemy
def enemy (x,y):
    screen.blit(img_enemy, (x,y))
# Game loop
is_running = True
while is_running:
    # RGB backgroung
    screen.blit(background ,(0,0))

    "player_x += 0.2"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            print("a key was pressed")
            if event.key == pygame.K_LEFT:
                print("left arrow pressed")
                player_x_change -= 0.5
            if event.key == pygame.K_RIGHT:
                print("RIGHT arrow pressed")
                player_x_change += 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Arrow keys were release")
                player_x_change = 0


    # update player location
    player_x += player_x_change

    # update enemy location
    enemy_x += enemy_x_change

    # keep player inside the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # keep enemy inside screen
    if enemy_x <= 0:
        enemy_x_change +=0.7
        enemy_y += enemy_y_change
    elif enemy_x >=736:
        enemy_x_change -=0.7
        enemy_y += enemy_y_change

    # show player
    player_x += player_x_change
    player(player_x,player_y)

    # show enemy
    enemy(enemy_x, enemy_y)

    # update screen
    pygame.display.update()


