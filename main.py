import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Bubble Sort")
icon = pygame.image.load('Diamond_Block-MC-Square.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('DOT-16.png')
playerX = 370
playerY = 535
playerY_change = 0
playerX_change = 0
tmpX = 0
tmpY = 0
playerScore = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Converting string to img for rendering text on window. There is no direct support for printing text on the window in 'pygame'
text_font = pygame.font.SysFont(None, 40)
def show_score(text, font, text_col):
    scoreImg = font.render(text, True, text_col)
    screen.blit(scoreImg, (370, 0))


# Balloons
balloonImg = pygame.image.load('balloon_64.png')
balloonX = 10
balloonY = 10


def balloon(x, y):
    screen.blit(balloonImg, (x, y))
    # screen.blit(playerScore, (370, 0))

# Game loop
running = True

while running:
    screen.fill((0, 180, 180))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0.1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.1
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0

    # pygame.display.flip()

    tmpY = playerY + playerY_change
    if 584 >= tmpY >= 30:
        playerY += playerY_change
    tmpX = playerX + playerX_change
    if 784 >= tmpX >= 0:
        playerX += playerX_change

    while (balloonX + 0) <= playerX <= (balloonX + 64) and (balloonY + 0) <= playerY <= (balloonY + 64):
        balloonX = random.randint(0, 736)
        balloonY = random.randint(50, 500)
        playerScore += 1


    show_score("Score : " + str(playerScore), text_font, (0, 0, 0))

    player(playerX, playerY)
    balloon(balloonX, balloonY)
    pygame.display.update()
