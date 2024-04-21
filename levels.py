import pygame
import os
import random
import math
import pytmx
from characters import SuperSonic, E102Gamma
from objects import *
from constants import *
from utils import Camera, draw_tiles

pygame.init()
pygame.mixer.init()

# The following code is for the EggmanLand zone which is only half working unfortunately. It can still be run if called.

# EggmanLandTMX = pytmx.load_pygame(os.path.join("assets", "world building", "Tiled Worlds", "Cityworld.tmx"))

# class Eggman_Land:
#     def __init__(self):
#         self.background_img = pygame.image.load(os.path.join("assets", "backgrounds", "EggmanLandBG.png")).convert()
#         self.background = pygame.transform.scale(self.background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
#         self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)  # Create an instance of Camera
#         self.sonic = Sonic(100, 300)
#         self.rings = pygame.sprite.Group()
#         self.enemies = pygame.sprite.Group()
#         self.load_rings()
#         self.load_enemies()
#         self.ring_counter = 0
#         self.show_target = False
#         self.tile_group = pygame.sprite.Group()  # Store tiles

#     def draw(self, screen):
#         screen.blit(self.background, (0, 0))
#         draw_tiles(screen, tmxdata=EggmanLandTMX, world_offset=[0, 0], camera=self.camera)
#         screen.blit(self.sonic.image, self.camera.apply(self.sonic.rect))
#         for ring in self.rings:
#             screen.blit(ring.image, self.camera.apply(ring.rect))  # Apply camera transformation to rings
        
#         for enemy in self.enemies:
#             screen.blit(enemy.image, self.camera.apply(enemy.rect))  # Apply camera transformation to enemies
        
#         ring_counter_display = RingFont.render("RINGS: " + str(self.ring_counter), True, (255, 255, 255))
#         screen.blit(ring_counter_display, (0, 0))
#         pygame.draw.rect(screen, "RED", self.camera.apply(self.sonic.hitbox), 2)

#     def load_rings(self):
#         num_rings = 5  # Number of rings
#         min_x, max_x = 100, 900  # Define the range for x coordinates
#         gap_width = (max_x - min_x) // (num_rings + 1)  # Calculate the width of each gap
#         y = 425  # Fix y coordinate

#         for i in range(1, num_rings + 1):
#             x = min_x + i * gap_width  # Calculate x coordinate for each ring
#             ring = Ring(x, y)  # Create ring object
#             self.rings.add(ring)  # Add ring to sprite group

#     def load_enemies(self):
#         pass

#     def update(self):
#         self.sonic.update()  # Update Sonic's position
        
#         # Generate tiles for ground and other layers if not already done
#         for layer_index, layer in enumerate(EggmanLandTMX.layers):
#             if layer.name != "nonCollideable":
#                 for x, y, image in layer.tiles():
#                     # Get the tile position in pixels
#                     tile_x = x * EggmanLandTMX.tilewidth
#                     tile_y = y * EggmanLandTMX.tileheight                    
#                     # Create tile instance and add it to the group
#                     tile_instance = Tile(image, (tile_x, tile_y))
#                     self.tile_group.add(tile_instance)

#         # Check for collisions between Sonic's rect and the tile rects
#         for tile in self.tile_group:
#             # Check for collision
#             if self.sonic.rect.colliderect(tile.rect):
#                 self.sonic.rect.bottom = tile.rect.top
#                 self.Yvel = 0
#                 # Sonic is grounded
#                 self.sonic.grounded = True
#                 # Reset jump flag
#                 if self.sonic.jumped:
#                     self.sonic.jumped = False
        
#         # Check for collisions between Sonic and rings
#         for ring in self.rings:
#             if pygame.sprite.collide_rect(ring, self.sonic):
#                 # Handle collision between Sonic and a ring
#                 ring.collectSound.play()  # Play collect sound
#                 ring.kill()
#                 self.ring_counter += 1
        
#         # Check for collisions between Sonic and enemies
#         for enemy in self.enemies:
#             enemy.update(self.sonic.rect)
#             if pygame.sprite.collide_mask(enemy, self.sonic):
#                 # Handle collision between Sonic and an enemy
#                 if self.sonic.homing:
#                     enemy.explode()
#                     self.show_target = False
        
#         # Update rings and enemies
#         self.rings.update()
#         self.enemies.update(self.sonic.rect)
#         # Update camera position based on Sonic's position
#         self.camera.update(self.sonic)

class BossfightZone:
    def __init__(self):
        self.initialize()

    def initialize(self):
        # Initialize the background and other assets
        self.background_img = pygame.image.load(os.path.join("assets", "backgrounds", "bossfightBG.png")).convert()
        self.background = pygame.transform.scale(self.background_img, (SCREEN_WIDTH * 20, SCREEN_HEIGHT * 4))
        self.background_x = 0
        self.background_y = 0
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player = SuperSonic(100, 300)
        self.rings = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.ring_counter = 10
        self.load_rings()
        self.boss = E102Gamma(15000, 1000)
        self.elapsed_time = 0
        self.gameEnded = False
        self.clock = pygame.time.Clock()
        self.gameovermusicPlayed = False
        self.HealthBar = HealthBar(self.boss, screen)

    def reset(self):
        # Reset all necessary variables to their initial state
        self.initialize()  # Re-initialize the class variables
        self.rings.empty()  # Clear any existing rings
        self.load_rings()  # Load new rings
        self.enemies.empty()  # Clear any existing enemies
        self.ring_counter = 10  # Reset the ring counter
        self.elapsed_time = 0  # Reset the elapsed time
        self.gameEnded = False  # Reset the game ended flag
        self.gameovermusicPlayed = False  # Reset the game over music flag

    def load_rings(self):
        num_ring_groups = 60  # Number of ring groups (300 rings in total)
        ring_gap = 176  # Gap between each ring in a group
        y_pos_min = 250  # Minimum Y position for a group of rings
        y_pos_max = 2000  # Maximum Y position for a group of rings

        for group_num in range(num_ring_groups):
            # Choose a random Y position between 250 and 550 for the group of rings
            group_y_pos = random.randint(y_pos_min, y_pos_max)           
            # Choose a random starting X position for the group of rings up to 4120
            x_pos_start = random.randint(500, 4120)           
            # Create a group of 5 rings with a gap of 176 between each ring
            for ring_num in range(5):
                # Calculate the X position for each ring in the group
                x_pos = x_pos_start + ring_num * ring_gap                
                # Create the ring at the calculated X and Y positions
                ring = Ring(x_pos, group_y_pos)                
                # Add the ring to the group of rings
                self.rings.add(ring)

    def draw(self, screen):
        # Draw the background twice for continuous scrolling
        screen.blit(self.background, self.camera.apply(self.background.get_rect())) 
               
        # Draw player and other sprites with camera transformation applied
        screen.blit(self.player.image, self.camera.apply(self.player.rect))
        screen.blit(self.boss.image, self.camera.apply(self.boss.rect))
        for laser in self.boss.bullet_group:
            screen.blit(laser.image, self.camera.apply(laser.rect))
        for ring in self.rings:
            screen.blit(ring.image, self.camera.apply(ring.rect))
        
        # Draw the ring counter and any additional HUD elements
        ring_counter_display = RingFont.render("RINGS: " + str(self.ring_counter), True, (255, 255, 255))
        screen.blit(ring_counter_display, (0, 0))
        
        self.HealthBar.draw()

    def update(self):
        self.player.update()  # Update Sonic's position
        self.boss.update(self.player)
        self.HealthBar.update()
        # Check if Sonic's Y position is less than 237 or more than 860
        if self.player.rect.y < 245:
            # Set Sonic's Y position to the minimum limit (237)
            self.player.rect.y = 245
        elif self.player.rect.y > 2500:
            # Set Sonic's Y position to the maximum limit (860)
            self.player.rect.y = 2500
        
        if pygame.sprite.collide_mask(self.player, self.boss) and not self.player.boosting and not self.player.taken_hit:
            self.ring_counter -= 1
            self.player.taken_hit = True
        self.player.immobile = False
        # Calculate the horizontal distance between the boss and the player
        distance = abs(self.boss.rect.x - self.player.rect.x)

        # Check if the distance is within a certain range (e.g., between 480 and 520)
        if 150 <= distance <= 800:
            self.boss.attack()
        elif 0 <= distance <= 150:
            self.boss.punch_attack(self.player)
        for laser in self.boss.bullet_group:
            if pygame.sprite.collide_mask(self.player, laser):
                if not self.player.taken_hit:
                    self.ring_counter -= 10
                    self.player.taken_hit = True
            self.player.taken_hit = False

        # Check for collisions between Sonic and rings
        for ring in self.rings:
            if pygame.sprite.collide_rect(ring, self.player):
                # Handle collision between Sonic and a ring
                ring.collectSound.play()  # Play collect sound
                ring.kill()
                self.ring_counter += 1

        dt = self.clock.get_time() / 1000.0
        print(f"Time elapsed this frame (dt): {dt}")  # Debug: print the time elapsed in the current frame

        self.elapsed_time += dt
        print(f"Total elapsed time: {self.elapsed_time}")  # Debug: print the total elapsed time

        # Check if one second has elapsed
        if self.elapsed_time >= 1:
            print("One second has passed!")  # Debug: notify when one second has passed

            # Decrease the ring counter by 1 if it is greater than 0
            if self.ring_counter > 0:
                self.ring_counter -= 1
                print(f"Ring counter decreased to: {self.ring_counter}")  # Debug: print the new ring counter value
            
            # Reset elapsed time
            self.elapsed_time = 0
            print("Elapsed time reset to 0")  # Debug: confirm that elapsed time is reset

        if self.ring_counter <= 0:
            self.gameEnded = True
        if self.boss.defeated:
            self.gameEnded = True

        # Update rings and enemies
        self.rings.update()
        
        # Update camera position based on Sonic's position
        self.camera.update(self.player)
        position = (self.player.rect.x, self.player.rect.y)
        print(position)
        print(self.boss.defeated)

    def gameOver(self, screen):
        GG = gameover_font.render("GAME OVER", True, (255, 255, 255))
        GGrect = GG.get_rect()
        screen.blit(GG, (((SCREEN_WIDTH // 2) - (GGrect.width // 2)), (SCREEN_HEIGHT//2) - GGrect.height))
        if pygame.mixer_music.get_busy():
            pygame.mixer_music.stop()
        pygame.mixer_music.load(os.path.join("assets", "music", "GameOver.mp3"))
        if not self.gameovermusicPlayed:
            pygame.mixer_music.play()
            self.gameovermusicPlayed = True
        pygame.time.wait(10000)