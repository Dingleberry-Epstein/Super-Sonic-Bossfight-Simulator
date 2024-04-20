import pygame, os, random, math, pytmx
from characters import Sonic
from objects import *
from constants import *
from utils import Camera, draw_tiles

pygame.init()
pygame.mixer.init()

EggmanLandTMX = pytmx.load_pygame(os.path.join("assets", "world building", "Tiled Worlds", "Cityworld.tmx"))

class Eggman_Land:
    def __init__(self):
        self.background_img = pygame.image.load(os.path.join("assets", "backgrounds", "EggmanLandBG.png")).convert()
        self.background = pygame.transform.scale(self.background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)  # Create an instance of Camera
        self.sonic = Sonic(100, 300)
        self.rings = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.load_rings()
        self.load_enemies()
        self.ring_counter = 0
        pygame.mixer.music.load(os.path.join(current_directory, "assets", "music", "Svidden - We Are.mp3"))
        self.show_target = False
        self.tile_group = pygame.sprite.Group()  # Store masks for ground tiles

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        draw_tiles(screen, tmxdata=EggmanLandTMX, world_offset=[0, 0], camera=self.camera)
        screen.blit(self.sonic.image, self.camera.apply(self.sonic.rect))
        for ring in self.rings:
            screen.blit(ring.image, self.camera.apply(ring.rect))  # Apply camera transformation to rings
        
        for enemy in self.enemies:
            screen.blit(enemy.image, self.camera.apply(enemy.rect))  # Apply camera transformation to enemies
        
        ring_counter_display = RingFont.render("RINGS: " + str(self.ring_counter), True, (255, 255, 255))
        screen.blit(ring_counter_display, (0, 0))

    def load_rings(self):
        num_rings = 5  # Number of rings
        min_x, max_x = 100, 900  # Define the range for x coordinates
        gap_width = (max_x - min_x) // (num_rings + 1)  # Calculate the width of each gap
        y = 425  # Fix y coordinate

        for i in range(1, num_rings + 1):
            x = min_x + i * gap_width  # Calculate x coordinate for each ring
            ring = Ring(x, y)  # Create ring object
            self.rings.add(ring)  # Add ring to sprite group

    def load_enemies(self):
        enemy1 = Enemy(600, 300, "roller")
        self.enemies.add(enemy1)

    def update(self):
        global homing_sound_played
        self.sonic.update()  # Update Sonic's position
        for layer in EggmanLandTMX.layers:
            # Iterate through each tile in the layer
            for x, y, gid in layer.tiles():
                # Get the tile properties for the current tile at position (x, y)
                tile_properties = EggmanLandTMX.get_tile_properties(x, y, 0)  # Layer index is 0, adjust as needed
                
                # Check if tile_properties is not None and contains the 'angle' property
                if tile_properties and 'angle' in tile_properties:
                    # Retrieve the angle of the tile (already in degrees)
                    ground_angle = tile_properties['angle']
                    print(f"Ground angle: {ground_angle}")
                    
                    # Calculate the change in Sonic's x position based on ground speed and ground angle
                    self.sonic.Xvel = self.sonic.groundSpeed * math.cos(ground_angle) * 2
                    if self.sonic.grounded:
                        if ground_angle > 0:
                            if self.sonic.groundSpeed < 0:
                                self.sonic.groundSpeed = -1 * self.sonic.groundSpeed
                            self.sonic.Yvel = 0
                            break
                else:
                    pass
        # Generate masks for ground tiles if not already done
        for layer in EggmanLandTMX.layers:
            if layer.name != "nonCollideable":
                for tile in layer.tiles():
                    tile_image = tile[2]
                    tile_pos_x = tile[0] * EggmanLandTMX.tilewidth
                    tile_pos_y = tile[1] * EggmanLandTMX.tileheight
                    tile_instance = Tile(tile_image, (tile_pos_x, tile_pos_y))
                    self.tile_group.add(tile_instance)
        # Check for collisions between Sonic's mask and the tile masks
        for tile in self.tile_group:
            offset_x = tile.rect.left - self.sonic.rect.left
            offset_y = tile.rect.top - self.sonic.rect.top
            if self.sonic.mask.overlap(tile.mask, (offset_x, offset_y)):
                self.sonic.grounded = True
                if self.sonic.jumped:
                    self.sonic.jumped = False
                break
        for tile in self.tile_group:
            offset_x = tile.rect.left - self.sonic.rect.left
            offset_y = tile.rect.top - self.sonic.rect.top
            if not self.sonic.mask.overlap(tile.mask, (offset_x, offset_y)):
                self.sonic.grounded = False
                break
        # Check for collisions between Sonic and rings
        for ring in self.rings:
            if pygame.sprite.collide_rect(ring, self.sonic):
                # Handle collision between Sonic and a ring
                ring.collectSound.play()  # Play collect sound
                ring.kill()
                self.ring_counter += 1
        
        # Check for collisions between Sonic and enemies
        for enemy in self.enemies:
            enemy.update(self.sonic.rect)
            if pygame.sprite.collide_mask(enemy, self.sonic):  # Check collision using masks
                # Handle collision between Sonic and an enemy
                if self.sonic.homing:
                    enemy.explode()
                    self.show_target = False
        
        # Update rings and enemies
        self.rings.update()
        self.enemies.update(self.sonic.rect)
        
        # Update camera position based on Sonic's position
        self.camera.update(self.sonic)