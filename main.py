import pygame
import random

from pygame import VIDEORESIZE


# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# Title and Icon
pygame.display.set_caption("Bubble Sort")
icon = pygame.image.load('Diamond_Block-MC-Square.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('DOT-16.png')
playerX = 1
playerY = 37
playerY_change = 0
playerX_change = 0
tmpX = 0
tmpY = 0
playerScore = 0
player_rect = playerImg.get_rect()


def show_player(x, y):
    screen.blit(playerImg, (x, y))


# Converting string to img for rendering text on window. There is no direct support for printing text on the window in 'pygame'
text_font = pygame.font.SysFont(None, 30)
text_font1 = pygame.font.SysFont(None, 50)
def show_score(text, font, text_col):
    scoreImg = font.render(text, True, text_col)
    screen.blit(scoreImg, (10, 10))


# Timer
clock = pygame.time.Clock()
start = 2599


def show_timer(text, font, text_col):
    timerImg = font.render(text, True, text_col)
    screen.blit(timerImg, ((screen.get_width() - 130), 10))


def show_randInt(text, font, text_col):
    randIntImg = font.render(text, True, text_col)
    screen.blit(randIntImg, (int(screen.get_width() / 2), 2))


b_img_1 = 'balloon_64-1.png'
b_img_2 = 'balloon_64-2.png'
b_img_3 = 'balloon_64-3.png'
b_img_4 = 'balloon_64-4.png'
b_img_5 = 'balloon_64-5.png'


class Balloon:

    def __init__(self, x, y, img_name):
        self.balloonX = x
        self.balloonY = y
        self.balloonImg = pygame.image.load(img_name)

    def show_balloon(self):
        screen.blit(self.balloonImg, (self.balloonX, self.balloonY))



I = 1
def b_choose():
    global I

    I = random.randint(1, 5)
    if I == 1:
        return b_img_1
    if I == 2:
        return b_img_2
    if I == 3:
        return b_img_3
    if I == 4:
        return b_img_4
    if I == 5:
        return b_img_5


def get_cord():
    x = random.randint(0, (screen.get_width() - 64))
    y = random.randint(53, (screen.get_height() - 100))
    return x, y


l1 = [(604, 114), (17, 170), (269, 285), (51, 146), (328, 424)]
res = [(604, 114), (17, 170), (269, 285), (51, 146), (328, 424)]

flg = 0
count = 0
cnt = 0
def get_cord_list():
    global count
    global flg
    count = 0
    for j in range(25):
        l1.append(get_cord())
        for i in l1:
            if count == 0:
                res.append(i)
                count += 1
            elif count == 1:
                flg = 0
                for k in range(1):
                    if (not(i[0] + 64) > res[k][0] > i[0]) and (not(i[1] + 64) > res[k][1] > i[1]) and (len(res) <= 4):
                        flg += 1
                if flg == 1:
                    res.append(i)
                    count += 1
            elif count == 2:
                flg = 0
                for k in range(2):
                    if (not(i[0] + 64) > res[k][0] > i[0]) and (not(i[1] + 64) > res[k][1] > i[1]) and (len(res) <= 4):
                        flg += 1
                if flg == 2:
                    res.append(i)
                    count += 1
            elif count == 3:
                flg = 0
                for k in range(3):
                    if (not(i[0] + 64) > res[k][0] > i[0]) and (not(i[1] + 64) > res[k][1] > i[1]) and (len(res) <= 4):
                        flg += 1
                if flg == 3:
                    res.append(i)
                    count += 1
            elif count == 4:
                flg = 0
                for k in range(4):
                    if (not(i[0] + 64) > res[k][0] > i[0]) and (not(i[1] + 64) > res[k][1] > i[1]) and (len(res) <= 4):
                        flg += 1
                if flg == 4:
                    res.append(i)
                    count += 1
        l1.clear()


def create_obj():
    global b1
    global b2
    global b3
    global b4
    global b5
    b1 = Balloon(res[0][0], res[0][1], b_img_1)
    b2 = Balloon(res[1][0], res[1][1], b_img_2)
    b3 = Balloon(res[2][0], res[2][1], b_img_3)
    b4 = Balloon(res[3][0], res[3][1], b_img_4)
    b5 = Balloon(res[4][0], res[4][1], b_img_5)


def show_balloons():
    b1.show_balloon()
    b2.show_balloon()
    b3.show_balloon()
    b4.show_balloon()
    b5.show_balloon()



# Game loop
cnt = 0
flg1 = 0
flg2 = 0
flag = 0
p_ratio_x = 0
p_ratio_y = 0
fullscreen = False
running = True
while running:

    global b1
    global b2
    global b3
    global b4
    global b5

    screen.fill((0, 180, 180))

    header_line = pygame.draw.line(screen, (0, 0, 0), (0, 35), (screen.get_width(), 35), 2)

    show_randInt(str(I), text_font1, (0, 0, 0))

    # Stopping game loop when timer over
    # if start < 0:
    #     running = False

    # For input from keyboard.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 5
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_f:
                # Getting the relative position of player and balloon to the size of fullscreen.
                p_ratio_x = playerX / screen.get_width()
                p_ratio_y = playerY / screen.get_height()
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    playerX = screen.get_width() * p_ratio_x
                    playerY = screen.get_height() * p_ratio_y
                else:
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                    # Reassigning the position of player and balloon according to the previous relative position in fullscreen mode.
                    playerX = screen.get_width() * p_ratio_x
                    playerY = screen.get_height() * p_ratio_y
                    flg1 = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0

    # Player clamping in window
    tmpY = playerY + playerY_change
    if (screen.get_height() - 16) >= tmpY >= 36:
        playerY += playerY_change
    tmpX = playerX + playerX_change
    if (screen.get_width() - 16) >= tmpX >= 0:
        playerX += playerX_change

    show_player(playerX, playerY)

    player_rect = pygame.Rect(playerX, playerY, 10, 10)

    if flg1 == 1:
        res.clear()
        l1.clear()
        get_cord_list()

    create_obj()

    b1_rect = pygame.Rect(b1.balloonX, b1.balloonY, 64, 64)
    b2_rect = pygame.Rect(b2.balloonX, b2.balloonY, 64, 64)
    b3_rect = pygame.Rect(b3.balloonX, b3.balloonY, 64, 64)
    b4_rect = pygame.Rect(b4.balloonX, b4.balloonY, 64, 64)
    b5_rect = pygame.Rect(b5.balloonX, b5.balloonY, 64, 64)


    #for checking the collision between balloons.
    for x in range(15):
        if b1_rect.colliderect(b2_rect):
            flg2 = 1
        elif b1_rect.colliderect(b3_rect):
            flg2 = 1
        elif b1_rect.colliderect(b4_rect):
            flg2 = 1
        elif b1_rect.colliderect(b5_rect):
            flg2 = 1
        elif b2_rect.colliderect(b3_rect):
            flg2 = 1
        elif b2_rect.colliderect(b4_rect):
            flg2 = 1
        elif b2_rect.colliderect(b5_rect):
            flg2 = 1
        elif b3_rect.colliderect(b4_rect):
            flg2 = 1
        elif b3_rect.colliderect(b5_rect):
            flg2 = 1
        elif b4_rect.colliderect(b5_rect):
            flg2 = 1

        if flg2 == 1:
            get_cord_list()
            create_obj()
            b1_rect = pygame.Rect(b1.balloonX, b1.balloonY, 64, 64)
            b2_rect = pygame.Rect(b2.balloonX, b2.balloonY, 64, 64)
            b3_rect = pygame.Rect(b3.balloonX, b3.balloonY, 64, 64)
            b4_rect = pygame.Rect(b4.balloonX, b4.balloonY, 64, 64)
            b5_rect = pygame.Rect(b5.balloonX, b5.balloonY, 64, 64)
        elif flg2 == 0:
            break

    show_balloons()

    if I == 1:
        tmp1 = b1_rect
    if I == 2:
        tmp1 = b2_rect
    if I == 3:
        tmp1 = b3_rect
    if I == 4:
        tmp1 = b4_rect
    if I == 5:
        tmp1 = b5_rect

    if player_rect.colliderect(tmp1):
        res.clear()
        l1.clear()
        get_cord_list()
        playerScore += 1
        flag = 1

    if flag == 1:
        choosenImg = b_choose()
        flag = 0

    show_score("Score : " + str(playerScore), text_font, (0, 0, 0))
    show_timer("Time : " + str(int(start / 100)), text_font, (0, 0, 0))
    start -= 1

    flg1 = 0

    clock.tick(100)
    pygame.display.update()
