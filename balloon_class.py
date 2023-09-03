import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)


# Balloons
# balloonImg = pygame.image.load('balloon_64-1.png')
# balloonX = random.randint(17, (screen.get_width() - 64))
# balloonY = random.randint(53, (screen.get_height() - 100))
#
# balloonImg2 = pygame.image.load('balloon_64-2.png')
# balloonX2 = random.randint(17, (screen.get_width() - 64))
# balloonY2 = random.randint(53, (screen.get_height() - 100))
#
# balloonImg3 = pygame.image.load('balloon_64-3.png')
# balloonX3 = random.randint(17, (screen.get_width() - 64))
# balloonY3 = random.randint(53, (screen.get_height() - 100))
#
# balloonImg4 = pygame.image.load('balloon_64-4.png')
# balloonX4 = random.randint(17, (screen.get_width() - 64))
# balloonY4 = random.randint(53, (screen.get_height() - 100))
#
# balloonImg5 = pygame.image.load('balloon_64-5.png')
# balloonX5 = random.randint(17, (screen.get_width() - 64))
# balloonY5 = random.randint(53, (screen.get_height() - 100))
#
#
# def b_respawn():
#     global balloonX
#     global balloonY
#     global balloonX2
#     global balloonY2
#     global balloonX3
#     global balloonY3
#     global balloonX4
#     global balloonY4
#     global balloonX5
#     global balloonY5
#     balloonX = random.randint(0, (screen.get_width() - 64))
#     balloonY = random.randint(40, (screen.get_height() - 100))
#     balloonX2 = random.randint(0, (screen.get_width() - 64))
#     balloonY2 = random.randint(40, (screen.get_height() - 100))
#     balloonX3 = random.randint(0, (screen.get_width() - 64))
#     balloonY3 = random.randint(40, (screen.get_height() - 100))
#     balloonX4 = random.randint(0, (screen.get_width() - 64))
#     balloonY4 = random.randint(40, (screen.get_height() - 100))
#     balloonX5 = random.randint(0, (screen.get_width() - 64))
#     balloonY5 = random.randint(40, (screen.get_height() - 100))
#
#
# def show_balloon(x, y, omg):
#     screen.blit(omg, (x, y))
#
#
# def b_load(b_name):
#     global balloonImg
#     balloonImg = pygame.image.load(b_name)
#
#
# def b_choose():
#     i = random.randint(1, 5)
#     if i == 1:
#         return balloonImg
#     if i == 2:
#         return balloonImg2
#     if i == 3:
#         return balloonImg3
#     if i == 4:
#         return balloonImg4
#     if i == 5:
#         return balloonImg5


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


def b_choose():
    i = random.randint(1, 5)
    if i == 1:
        return b_img_1
    if i == 2:
        return b_img_2
    if i == 3:
        return b_img_3
    if i == 4:
        return b_img_4
    if i == 5:
        return b_img_5


def get_cord():
    x = random.randint(0, (screen.get_width() - 64))
    y = random.randint(53, (screen.get_height() - 100))
    return x, y


l1 = [(604, 114), (17, 170), (269, 285), (51, 146), (328, 424)]
res = [(604, 114), (17, 170), (269, 285), (51, 146), (328, 424)]

flg = 0
count = 0
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


run = True
while run:
    # cnt += 1
    screen.fill((0, 180, 180))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # print(cnt)
    b1 = Balloon(res[0][0], res[0][1], b_img_1)
    b1.show_balloon()
    b2 = Balloon(res[1][0], res[1][1], b_img_2)
    b2.show_balloon()
    b3 = Balloon(res[2][0], res[2][1], b_img_3)
    b3.show_balloon()
    b4 = Balloon(res[3][0], res[3][1], b_img_4)
    b4.show_balloon()
    b5 = Balloon(res[4][0], res[4][1], b_img_5)
    b5.show_balloon()

    # show_balloon(balloonX, balloonY, balloonImg)
    # show_balloon(balloonX2, balloonY2, balloonImg2)
    # show_balloon(balloonX3, balloonY3, balloonImg3)
    # show_balloon(balloonX4, balloonY4, balloonImg4)
    # show_balloon(balloonX5, balloonY5, balloonImg5)


    res.clear()
    l1.clear()

    get_cord_list()

    clock.tick(3)

    pygame.display.update()
