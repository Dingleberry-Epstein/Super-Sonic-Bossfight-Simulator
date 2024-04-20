import os
import pygame
from pygame.locals import *
from characters import *
from constants import *
from levels import Eggman_Land
pygame.init()
pygame.mixer.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonic Game ")
runwindmillisle = False
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if  event.key == K_RETURN:
                windmillisle = Eggman_Land()
                runwindmillisle = True
                pygame.mixer_music.play()
            if event.key == K_ESCAPE:
                screen.fill("BLACK")
                screen.blit((gameover_font.render("QUITTING THE GAME...", True, (255, 255, 255))), ((SCREEN_WIDTH//2) - 300, SCREEN_HEIGHT//2))
                runwindmillisle = False
                if runwindmillisle == False:
                    running = False
    if runwindmillisle:
        windmillisle.update()
        windmillisle.draw(screen)
        FPScounter = pygame.time.Clock.get_fps(clock)
        FPScounter_display = RingFont.render("FPS:" + str(int(FPScounter)), True, ("WHITE"))
        screen.blit(FPScounter_display, (1160, 0))
    pygame.display.flip()
    clock.tick(60)
# Quit the game 
pygame.quit()