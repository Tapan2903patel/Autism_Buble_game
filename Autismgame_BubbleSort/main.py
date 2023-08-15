import pygame
import random
from pygame import mixer  # for music & sound effects

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
bg = pygame.image.load('white-cloud-blue-sky-sea.jpg')
sad = pygame.image.load('sad_balloon (2).png')
game_over_text = pygame.font.Font('freesansbold.ttf', 63)


def show_game_over():
    game_over = game_over_text.render("GAME OVER ", True, (0, 0, 0))

    scaled_background = pygame.transform.scale(bg, (screen.get_width(), screen.get_height()))
    screen.blit(scaled_background, (0, 0))

    screen.blit(sad, ((2 * screen.get_width() // 3), screen.get_height() - 520))
    screen.blit(sad, ((17.5 * screen.get_width() // 20), screen.get_height() - 297))
    # screen.blit(sad, (screen.get_width()-705, 437))
    # screen.blit(sad, ((screen.get_width() // 3) + 100, screen.get_height() - 520))
    # screen.blit(sad, ((689, screen.get_height() - 520)))
    # screen.blit(sad, ((4.37 * screen.get_width() // 5), screen.get_height() - 200))
    screen.blit(sad, ((1.2 * screen.get_width() // 13), screen.get_height() - 150))
    screen.blit(sad, (screen.get_width() - 750, 100))
    screen.blit(sad, (screen.get_width() - 1165, 89))

    game_over_rect = game_over.get_rect(center=((2.9 * screen.get_width() // 5) - 48, screen.get_height() - 430))
    screen.blit(game_over, game_over_rect)

    show_score((2 * screen.get_width() // 5) - 7, screen.get_height() - 330, 35, (0, 0, 0))

    mouse_pos = pygame.mouse.get_pos()
    if game_over_rect.collidepoint(mouse_pos):
        game_over = game_over_text.render("GAME OVER ", True, (20, 0, 225))
        screen.blit(game_over, game_over_rect)


def show_player(x, y):
    screen.blit(playerImg, (x, y))


# Converting string to img for rendering text on window. There is no direct support for printing text on the window in 'pygame'
text_font = pygame.font.SysFont(None, 30)
text_font1 = pygame.font.SysFont(None, 50)


def show_score(x, y, size, text_col):
    score = pygame.font.Font('freesansbold.ttf', size)
    final_score = score.render("Score : " + str(playerScore), True, text_col)
    # scoreImg = font.render(text, True, text_col)
    screen.blit(final_score, (x, y))


# Timer
clock = pygame.time.Clock()
start = 2599


def show_timer(x, y, text, font, text_col):
    timerImg = font.render(text, True, text_col)
    screen.blit(timerImg, (x, y))


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

    # def remove_balloons(self,x,y):

    def get_ratio(self):
        self.b_ratio_x = b1.balloonX / screen.get_width()
        self.b_ratio_y = b1.balloonY / screen.get_height()
        print(self.b_ratio_x)

    def reposition(self):
        self.balloonX = int(screen.get_width() * self.b_ratio_x)
        self.balloonY = int(screen.get_height() * self.b_ratio_y)


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
                    if (not (i[0] + 64) > res[k][0] > i[0]) and (not (i[1] + 64) > res[k][1] > i[1]) and (
                            len(res) <= 4):
                        flg += 1
                if flg == 1:
                    res.append(i)
                    count += 1
            elif count == 2:
                flg = 0
                for k in range(2):
                    if (not (i[0] + 64) > res[k][0] > i[0]) and (not (i[1] + 64) > res[k][1] > i[1]) and (
                            len(res) <= 4):
                        flg += 1
                if flg == 2:
                    res.append(i)
                    count += 1
            elif count == 3:
                flg = 0
                for k in range(3):
                    if (not (i[0] + 64) > res[k][0] > i[0]) and (not (i[1] + 64) > res[k][1] > i[1]) and (
                            len(res) <= 4):
                        flg += 1
                if flg == 3:
                    res.append(i)
                    count += 1
            elif count == 4:
                flg = 0
                for k in range(4):
                    if (not (i[0] + 64) > res[k][0] > i[0]) and (not (i[1] + 64) > res[k][1] > i[1]) and (
                            len(res) <= 4):
                        flg += 1
                if flg == 4:
                    res.append(i)
                    count += 1
        l1.clear()


# Game loop
flag = 0
p_ratio_x = 0
p_ratio_y = 0
fullscreen = False
running = True
# Game over loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear the screen

    if start < 0:
        show_game_over()

        # Display replay and exit options
        replay_text = text_font1.render("Replay", True, (0, 0, 0))
        exit_text = text_font1.render("Exit", True, (0, 0, 0))
        replay_rect = replay_text.get_rect(center=(screen.get_width() // 3, screen.get_height() - 100))
        exit_rect = exit_text.get_rect(center=(2 * screen.get_width() // 3, screen.get_height() - 100))
        screen.blit(replay_text, replay_rect)
        screen.blit(exit_text, exit_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()

        # Check if the mouse is over the replay button
        if replay_rect.collidepoint(mouse_pos):
            replay_text = text_font1.render("Replay", True, (255, 0, 0))
            screen.blit(replay_text, replay_rect)

            if mouse_clicked[0]:  # Left mouse button clicked
                start = 2599  # Reset the timer
                playerScore = 0  # Reset the score
                res.clear()
                l1.clear()
                get_cord_list()  # Generate new balloon positions
                I = random.randint(1, 5)  # Choose a new balloon type

        # Check if the mouse is over the exit button
        if exit_rect.collidepoint(mouse_pos):
            exit_text = text_font1.render("Exit", True, (255, 0, 0))
            screen.blit(exit_text, exit_rect)

            if mouse_clicked[0]:  # Left mouse button clicked
                running = False  # Exit the game

    else:
        screen.fill((0, 180, 180))

        header_line = pygame.draw.line(screen, (0, 0, 0), (0, 35), (screen.get_width(), 35), 2)

        show_randInt(str(I), text_font1, (0, 0, 0))

        b1 = Balloon(res[0][0], res[0][1], b_img_1)
        b2 = Balloon(res[1][0], res[1][1], b_img_2)
        b3 = Balloon(res[2][0], res[2][1], b_img_3)
        b4 = Balloon(res[3][0], res[3][1], b_img_4)
        b5 = Balloon(res[4][0], res[4][1], b_img_5)

        # For input from keyboard.

        # Player clamping in window
        tmpY = playerY + playerY_change
        if (screen.get_height() - 16) >= tmpY >= 36:
            playerY += playerY_change
        tmpX = playerX + playerX_change
        if (screen.get_width() - 16) >= tmpX >= 0:
            playerX += playerX_change

        show_player(playerX, playerY)

        b1.show_balloon()
        # print(b1.b_ratio_x)
        b2.show_balloon()
        b3.show_balloon()
        b4.show_balloon()
        b5.show_balloon()

        if I == 1:
            tmp = b1
        if I == 2:
            tmp = b2
        if I == 3:
            tmp = b3
        if I == 4:
            tmp = b4
        if I == 5:
            tmp = b5

        if (tmp.balloonX + 0) <= playerX <= (tmp.balloonX + 64) and (tmp.balloonY + (-10)) <= playerY <= (
                tmp.balloonY + 64):
            res.clear()
            l1.clear()
            get_cord_list()
            pop_sound = mixer.Sound('balloon_pop.wav')
            pop_sound.play()
            playerScore += 1
            flag = 1
        if (flag == 1):
            choosenImg = b_choose()
            flag = 0
        start -= 1
        clock.tick(100)
        show_score(10, 10, 20, (0, 0, 0))
        show_timer((screen.get_width() - 130), 10, "Time : " + str(int(start / 100)), text_font, (0, 0, 0))

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
                b1.get_ratio()
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                    # Reassigning the position of player and balloon according to the previous relative position in fullscreen mode.
                    playerX = screen.get_width() * p_ratio_x
                    playerY = screen.get_height() * p_ratio_y
                    b1.reposition()
                    # print(b1.balloonX)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0

    pygame.display.update()
