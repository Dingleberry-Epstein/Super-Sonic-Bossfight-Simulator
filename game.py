import os
import pygame
from pygame.locals import *
from characters import *
from constants import *
from levels import BossfightZone
from utils import *
pygame.mixer.init()

class SonicGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Super Sonic Bossfight Simulator!!")
        self.clock = pygame.time.Clock()
        self.game_state = 'intro'
        self.gameplay_running = False
        self.running = True
        self.bgIMG = pygame.image.load(os.path.join("assets", "backgrounds", "bg.jpg"))
        self.background_image = pygame.transform.scale(self.bgIMG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.mixer.music.load(os.path.join("assets", "music", "Through The Gates.mp3"))
        self.loading_screen_img = pygame.image.load(os.path.join("assets", "backgrounds", "LOADING_SCREEN.png"))
        self.loading_screen_fade_in = False
        self.loading_screen_fade_out = False
        self.intro_duration = [3, 2, 1]
        self.intro_images = [
            pygame.image.load(os.path.join("assets", "SEGA_logo.png")).convert_alpha(),
            pygame.image.load(os.path.join("assets", "Sonic_Team_Logo.png")).convert_alpha(),
            pygame.image.load(os.path.join("assets", "Migglesoft.png")).convert_alpha(),
        ]
        self.level = BossfightZone()  # Create an instance of BossfightZone
        self.victory_music_played = False

    def run_intro(self):
        pygame.mixer.music.play(-1)
        index = 0
        while self.running and index < len(self.intro_images):
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    break

            fade_in_out(self.intro_images[index], self.intro_duration[index])
            index += 1

        scene_fade_in(self.screen, self.clock, self.background_image, 1)
        START = MenuFont.render("Press any key to begin!", True, (0, 0, 0))
        STARTrect = START.get_rect()
        self.screen.blit(START, (((SCREEN_WIDTH // 2) - (STARTrect.width // 2)), SCREEN_HEIGHT * 0.75))
        self.game_state = 'menu'

    def run_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_ESCAPE:
                    self.game_state = 'loading_screen'
                else:
                    self.running = False

    def run_loading_screen(self):
        self.screen.fill("BLACK")
        if not self.loading_screen_fade_in:
            scene_fade_in(self.screen, self.clock, self.loading_screen_img, 1)
            self.loading_screen_fade_in = True
                # Reset necessary flags and states here
        self.level.reset()  # Make sure to reset the level
        self.level.gameovermusicPlayed = False  # Reset this flag for future game overs
        screen.blit(self.loading_screen_img, (0, 0))
        pygame.display.update()  # Update the screen to show changes
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.mixer_music.fadeout(500)
                pygame.mixer_music.load(os.path.join("assets", "music", "BOSS BATTLE _ BIG ARM.mp3"))
                pygame.mixer_music.play(-1)
                if not self.loading_screen_fade_out:
                    scene_fade_out(self.screen, self.clock, self.loading_screen_img, 5, "BLACK")
                    self.loading_screen_fade_out = True
                self.game_state = 'in_game'

    def run_gameplay(self):
        self.screen.fill("BLACK")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return

        if not self.level.gameEnded and not self.level.boss.defeated:
            # Game is still running, update and draw the level
            self.level.update()
            self.level.draw(self.screen)
            # Display FPS counter
            FPScounter = self.clock.get_fps()
            FPScounter_display = RingFont.render(f"FPS: {int(FPScounter)}", True, (255, 255, 255))
            self.screen.blit(FPScounter_display, (1160, 0))

        elif self.level.gameEnded and not self.level.boss.defeated:
            # If the game has ended without defeating the boss
            pygame.mixer.stop()
            self.screen.fill("BLACK")
            self.level.gameOver(self.screen)
            if not pygame.mixer.music.get_busy():
                self.game_state = 'loading_screen'

        elif self.level.boss.defeated and self.level.gameEnded:
            self.screen.fill("BLACK")
            pygame.mixer.stop()
            if not self.victory_music_played:
                pygame.mixer.music.load(os.path.join("assets", "music", "Victory.mp3"))
                pygame.mixer.music.play()
                self.victory_music_played = True

            # Display victory message
            # Display victory message
            victory_message = gameover_font.render("YOU DID IT!", True, (255, 255, 255))
            victory_rect = victory_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(victory_message, victory_rect)

            # Display "Press ESC to quit game" message
            exit_message = RingFont.render("Press ESC to quit game", True, (255, 255, 255))
            exit_rect = exit_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            self.screen.blit(exit_message, exit_rect)

            # Handle key press to quit the game
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.running = False
                pygame.quit()    

    def run_game(self):
        while self.running:
            if self.game_state == 'intro':
                self.run_intro()
            elif self.game_state == 'menu':
                self.run_menu()
            elif self.game_state == 'loading_screen':
                self.run_loading_screen()
            elif self.game_state == 'in_game':
                self.run_gameplay()
                self.gameplay_running = True

            pygame.display.update()
            self.clock.tick(60)  # Limit the game loop to 60 FPS

        pygame.quit()