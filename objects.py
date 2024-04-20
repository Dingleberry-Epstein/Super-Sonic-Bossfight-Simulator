import pygame, os, math

from constants import *
from utils import Button
platX = 10
platY = 500
platW = 5000
platH = 47
testbgX = 0
testbgY = 0
testbgW = 1728
testbgH = 1080
test_platform = pygame.Rect(platX, platY, platW, platH)
testbg_rect = pygame.Rect(testbgX, testbgY, testbgW, testbgH)

platform_img1 = pygame.image.load(os.path.join("assets", "world building", "HUBGround.png"))

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, position, points=None):
        super().__init__()
        self.image = image.convert_alpha()
        if points is not None:  # If points are provided, it's a slope
            self.image.fill((0, 0, 0, 0))  # Clear the image for transparency
            pygame.draw.polygon(self.image, (0, 255, 0), points)  # Draw a slope
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.image)

class Ring(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.imageLoad = [pygame.image.load(os.path.join("assets", "sprites", "ring", f"ring{i}.png")).convert_alpha() for i in range(1, 9)]
        self.images = [pygame.transform.scale(image, (50, 50)) for image in self.imageLoad]
        self.rect = self.images[0].get_rect()
        self.rect.topleft = (x, y)
        self.collectSound = pygame.mixer.Sound(os.path.join("assets", "sounds", "collectring.mp3"))
        self.frame = 0
        self.animation_speed = 0.1

    def update(self):
        # Update animation frame based on animation speed
        self.frame += self.animation_speed
        self.frame %= len(self.images)
        self.image = self.images[int(self.frame)]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.enemy_type = enemy_type
        self.width = 40
        self.height = 40
        self.animation_speed = 200
        self.explosion_animation_speed = 75
        self.current_frame = 0
        self.animation_frames = [pygame.image.load(os.path.join("assets", "sprites", "Badniks", f"badnikroller{i}.png")).convert_alpha() for i in range(1, 5)]  # Load animation frames here
        self.image = self.animation_frames[self.current_frame]  # Placeholder image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.velocity = 1  # Velocity for moving enemies
        self.gravity = 5
        self.last_update = pygame.time.get_ticks()
        self.death_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "explosion.mp3"))
        self.death_sound_played = False
        self.explosion_frames = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "Badniks", f"explosion{i}.png")).convert_alpha(), (160, 160)) for i in range(1, 18)]
        self.alive = True
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, player_rect):
        if self.enemy_type == "roller":
            if self.alive:
                if self.rect.x < player_rect.x:
                    self.rect.x += self.velocity
                    self.direction = -1
                elif self.rect.x > player_rect.x:
                    self.rect.x -= self.velocity
                    self.direction = 1
                now = pygame.time.get_ticks()
                if now - self.last_update > self.animation_speed:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
                    if self.direction == 1:
                        self.image = self.animation_frames[self.current_frame]
                    elif self.direction == -1:
                        self.image = pygame.transform.flip(self.animation_frames[self.current_frame], True, False)
            else:
                now = pygame.time.get_ticks()
                if now - self.last_update > self.explosion_animation_speed:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.explosion_frames)
                    if self.direction == 1:
                        self.image = self.explosion_frames[self.current_frame]
                    elif self.direction == -1:
                        self.image = pygame.transform.flip(self.explosion_frames[self.current_frame], True, False)
                self.rect.y = 350

        if hasattr(self, 'explosion_start_time'):
            if pygame.time.get_ticks() - self.explosion_start_time >= 1000:
                self.kill()

        # Check for collision with player

    def explode(self):
        self.alive = False
        if not self.death_sound_played:
            self.death_sound.play()
            self.death_sound_played = True
        self.explosion_start_time = pygame.time.get_ticks()  # Record the start time of the explosion
