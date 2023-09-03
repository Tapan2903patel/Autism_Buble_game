import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()
start = 600


text_font = pygame.font.SysFont(None, 40)
def show_score(text, font, text_col):
    scoreImg = font.render(text, True, text_col)
    screen.blit(scoreImg, (150, 130))


finished = False
while not finished:

    screen.fill((0, 0, 0))

    show_score("Time : " + str(int(start/100)), text_font, (255, 255, 255))
    start -= 1

    if start <= 0:
        finished = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    clock.tick(100)

    pygame.display.update()
