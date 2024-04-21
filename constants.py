import pygame
import os


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)

pygame.mixer.init()
pygame.font.init()
current_directory = os.path.dirname(__file__)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

testbg = pygame.image.load(os.path.join("assets", "backgrounds",  "HUB.png")).convert()
platSprite = pygame.image.load(os.path.join("assets", "world building",  "HUBGround.png")).convert()

fallSound = pygame.mixer.Sound(os.path.join("assets", "sounds" , "fall.mp3"))
jumpSound = pygame.mixer.Sound(os.path.join("assets", "sounds" , "Jumpsound.wav"))
stoppingSound = pygame.mixer.Sound(os.path.join("assets", "sounds" , "Brake.mp3"))

gameover_font = pygame.font.Font(os.path.join("assets", "doom.ttf"), 128)
GAMEOVER = gameover_font.render("GAME OVER", True, (0, 0, 0))
GAMEOVER_rect = GAMEOVER.get_rect()
GAMEOVER_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
RingFont = pygame.font.Font(os.path.join("assets", "ReFormation Sans Regular.ttf"), 32)
MenuFont = pygame.font.Font(os.path.join("assets", "doom.ttf"), 64)

TryAgain = gameover_font.render("Try Again?", True, (255, 255, 255))
TryAgain_rect = TryAgain.get_rect()
TryAgain_rect.center = (SCREEN_WIDTH//2, (SCREEN_HEIGHT//2) - 20)

select_sound = pygame.mixer.Sound(os.path.join("assets", "sounds" , "SelectSound.mp3"))
hover_sound = pygame.mixer.Sound(os.path.join("assets", "sounds" , "HoverSound.mp3"))

original_homing_image = pygame.image.load(os.path.join("assets", "sprites", "Homing Attack", "homing1.png")).convert_alpha()
homing_image = pygame.transform.scale(original_homing_image, (67.5, 67.5))
homing_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "homingsound.mp3"))
homing_sound_played = False