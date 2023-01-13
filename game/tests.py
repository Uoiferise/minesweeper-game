import pygame
import sys
from settings import *

pygame.init()

screen = pygame.display.set_mode(RES)
# r = pygame.Rect(0, 0, 40, 40)
# pygame.draw.rect(screen, (100, 100, 100), r, 0)
# r = pygame.Rect(360, 360, 400, 400)
# pygame.draw.rect(screen, (100, 100, 100), r, 0)

for i in range(1, 10):
    pygame.draw.line(screen, (100, 100, 100), (i * 40 - 2, 0), (i * 40 - 2, 400), width=3)
    pygame.draw.line(screen, (100, 100, 100), (0, i * 40 - 2), (400, i * 40 - 2), width=3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)

    pygame.display.flip()
