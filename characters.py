import pygame, math, random
from constants import *
from objects import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
pygame.mixer.init()

# This is the Sonic class which contains the original code for Sonic and his angled movement. The code does work however it doesn't function as intended.
# The code is left here for reference. It can still be called, however it must be called into an instance of EggmanLand.

# class Sonic(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.x = int(x)
#         self.y = int(y)
#         self.frame = 0
#         self.width = 40 
#         self.height = 40
#         self.run_images = [pygame.image.load(os.path.join("assets", "sprites", "Sonic", f"SonicRun{i}.png")).convert_alpha() for i in range(1, 9)]
#         self.sprint_images = [pygame.image.load(os.path.join("assets", "sprites", "Sonic", f"SonicSprint{i}.png")).convert_alpha() for i in range(1, 9)]
#         self.boosting_images = [pygame.image.load(os.path.join("assets", "sprites", "Sonic", f"SonicBoost{i}.png")).convert_alpha() for i in range(1, 9)]
#         self.idle_images = [pygame.image.load(os.path.join("assets", "sprites", "Sonic", f"SonicIdle{i}.png")).convert_alpha() for i in range(1, 6)]
#         self.jump_images = [pygame.image.load(os.path.join("assets", "sprites", "Sonic", f"SonicJump{i}.png")).convert_alpha() for i in range(1, 5)]
#         self.stopping_images = [pygame.image.load(os.path.join("assets", "sprites", "Sonic", f"SonicStopping{i}.png")).convert_alpha() for i in range(1, 3)]
#         self.gameover_images = [pygame.image.load(os.path.join("assets", "sprites", "Sonic", f"sonicfall{i}.png")).convert_alpha() for i in range(1, 6)]
#         self.image_index = 0
#         self.image = self.idle_images[self.image_index]  # Index to track the current animation frame
#         self.rect = self.image.get_rect(topleft=(self.x, self.y)) # Get the rectangle that encloses the square
#         self.hitbox = pygame.Rect(((self.rect.x//2) + 100),(self.rect.y +50), (self.rect.width//2), (self.rect.height * 0.8))
#         self.animation_speed = 0.1
#         self.acceleration = 0.2  # Initial acceleration
#         self.max_acceleration = 0.3  # Maximum acceleration
#         self.deceleration = 0.5
#         self.friction = 0.46875
#         self.maxSpeed = 33
#         self.groundSpeed = 0
#         self.gravityforce = 0.5
#         self.angle = 0
#         self.jumped = False
#         self.direction = 0
#         self.Yvel = 0
#         self.jumpSoundPlayed = False
#         self.gameover = False
#         self.homing = False
#         self.target_enemy = None
#         self.grounded = False
#         self.stopping = False
#         self.stoppingSoundPlayed = False
#         self.mask = pygame.mask.from_surface(self.image)
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE] and not self.jumped:  # Check if Space key is pressed and Sonic hasn't jumped yet
#             self.Yvel = -15
#             self.jumped = True
#             self.grounded = False
#             if not self.jumpSoundPlayed:
#                 pygame.mixer.Sound.play(jumpSound)
#                 self.jumpSoundPlayed = True
#             self.jumpSoundPlayed = False  # Update the flag to indicate that the jump sound has been played
#         if keys[pygame.K_LEFT] or keys[pygame.K_a]:
#             self.direction = 1
#             if self.groundSpeed > 0:
#                 self.groundSpeed -= self.deceleration
#                 self.stopping = True
#                 if self.groundSpeed <= 0:
#                     self.groundSpeed = -0.5
#                     self.stopping = False
#             elif self.groundSpeed > -self.maxSpeed:
#                 # Gradually increase acceleration up to maximum
#                 if self.acceleration < self.max_acceleration:
#                     self.acceleration += 0.001
#                 if self.acceleration > self.max_acceleration:
#                     self.acceleration = self.max_acceleration
#                 self.groundSpeed -= self.acceleration
#                 if self.groundSpeed <= -self.maxSpeed:
#                     self.groundSpeed = -self.maxSpeed
#         elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#             self.direction = -1
#             if self.groundSpeed < 0:
#                 self.groundSpeed += self.deceleration
#                 self.stopping = True
#                 if self.groundSpeed >= 0:
#                     self.groundSpeed = 0.5
#                     self.stopping = False
#             elif self.groundSpeed < self.maxSpeed:
#                 # Gradually increase acceleration up to maximum
#                 if self.acceleration < self.max_acceleration:
#                     self.acceleration += 0.001
#                 if self.acceleration > self.max_acceleration:
#                     self.acceleration = self.max_acceleration
#                 self.groundSpeed += self.acceleration
#                 if self.groundSpeed >= self.maxSpeed:
#                     self.groundSpeed = self.maxSpeed
#         else:
#             if self.acceleration > 0.05:
#                 self.acceleration -= 0.001
#             self.groundSpeed -= min(abs(self.groundSpeed), self.friction) * (self.groundSpeed / abs(self.groundSpeed) if self.groundSpeed != 0 else 0)
#             self.stopping = False
#         if self.stopping and not self.jumped:
#             if not self.stoppingSoundPlayed:
#                 stoppingSound.play()
#                 self.stoppingSoundPlayed = True
#         if self.stoppingSoundPlayed == True and not self.stopping:
#             self.stoppingSoundPlayed = False

#         if not self.grounded:
#             self.Yvel += self.gravityforce
#         self.x += self.groundSpeed
#         self.rect.x = self.x  # Update self.rect with the new x coordinate
#         self.y += self.Yvel
#         self.rect.y = self.y
#         self.hitbox.x = self.x
#         self.hitbox.y = self.y
#         # Update animation speed and direction
#         self.update_animation()

#     def update_animation(self):
#         # Calculate animation speed based on Sonic's ground speed
#         self.animation_speed = min(0.1 + abs(self.groundSpeed) * 0.01, 0.5)

#         # Update animation frame based on animation speed
#         self.frame += self.animation_speed
#         self.image_index = int(self.frame) % len(self.run_images)

#         # Update Sonic's image
#         if self.groundSpeed > 0 and not self.jumped and not self.stopping:
#             if self.groundSpeed < 15:
#                 self.image = self.run_images[self.image_index]
#             elif self.groundSpeed > 15:
#                 self.image = self.sprint_images[self.image_index]
#             elif self.groundSpeed > 30:
#                 self.image = self.boosting_images[self.image_index]
#         elif self.groundSpeed < 0 and not self.jumped and not self.stopping:
#             if self.groundSpeed > -15:
#                 self.image = pygame.transform.flip(self.run_images[self.image_index], True, False)
#             elif self.groundSpeed < -15:
#                 self.image = pygame.transform.flip(self.sprint_images[self.image_index], True, False)
#             elif self.groundSpeed < -30:
#                 self.image = pygame.transform.flip(self.boosting_images[self.image_index], True, False)
#         elif self.groundSpeed == 0 and not self.jumped and not self.stopping:
#             self.image_index = int(self.frame) % len(self.idle_images)
#             if self.direction == -1:
#                 self.image = self.idle_images[self.image_index]
#             elif self.direction == 1:
#                 self.image = pygame.transform.flip(self.idle_images[self.image_index], True, False)

#         if self.jumped:
#             jump_image_count = len(self.jump_images)
#             self.image_index = int(self.frame) % jump_image_count
#             if self.groundSpeed > 0:
#                 self.image = self.jump_images[self.image_index]
#             elif self.groundSpeed < 0:
#                 self.image = pygame.transform.flip(self.jump_images[self.image_index], True, False)
#             else:
#                 if self.direction == -1:
#                     self.image = self.jump_images[self.image_index]
#                 elif self.direction == 1:
#                     self.image = pygame.transform.flip(self.jump_images[self.image_index], True, False)

#         if self.stopping and not self.jumped:
#             stopping_image_count = len(self.stopping_images)
#             self.image_index = int(self.frame) % stopping_image_count
#             if self.direction == 1:
#                 self.image = self.stopping_images[self.image_index]
#             elif self.direction == -1:
#                 self.image = pygame.transform.flip(self.stopping_images[self.image_index], True, False)

class SuperSonic():
    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.frame = 0
        self.width = 40 
        self.height = 40
        self.idle_images = [pygame.image.load(os.path.join("assets", "sprites", "Super Sonic", f"supersonic{i}.png")).convert_alpha() for i in range(1, 3)]
        self.fly_images = [pygame.image.load(os.path.join("assets", "sprites", "Super Sonic", f"supersonicfly{i}.png")).convert_alpha() for i in range(1, 7)]
        self.boosting_images = [pygame.image.load(os.path.join("assets", "sprites", "Super Sonic", f"supersonicboost{i}.png")).convert_alpha() for i in range(1, 5)]
        self.image_index = 0
        self.image = self.idle_images[self.image_index]  # Index to track the current animation frame
        self.rect = self.image.get_rect(topleft=(self.x, self.y)) # Get the rectangle that encloses the square
        self.animation_speed = 0.1
        self.gameover = False
        self.direction = 0
        self.vertical_direction = 0
        self.boostfactor = 2
        self.speedfactor = 20
        self.current_speed = 0
        self.boosting = False
        self.mask = pygame.mask.from_surface(self.image)
        self.boost_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "sonic boom.mp3"))
        self.boost_sound_played = False
        self.fire_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "fire.mp3"))
        self.fire_sound_played = False
        self.wind_noise = pygame.mixer.Sound(os.path.join("assets", "sounds", "wind.mp3"))
        self.wind_noise_played = False
        self.taken_hit = False
        self.immobile = False
    def update(self):
        keys = pygame.key.get_pressed()
        if self.taken_hit:
            self.immobile = True
        else:
            self.immobile = False

        if not self.immobile:
            # Determine if Sonic is moving
            moving = keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]
        else:
            moving = False

        # Set the current speed based on movement and boost (space key)
        if moving:
            self.current_speed = self.speedfactor * self.boostfactor if keys[pygame.K_SPACE] else self.speedfactor
        else:
            self.current_speed = 0

        # Movement handling
        move_x = 0  # Initialize movement in x-direction
        move_y = 0  # Initialize movement in y-direction

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            move_x -= self.current_speed
            self.direction = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            move_x += self.current_speed
            self.direction = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            move_y -= self.current_speed
            self.vertical_direction = 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            move_y += self.current_speed
            self.vertical_direction = -1

        # Update Sonic's position based on x and y movement
        self.x += move_x
        self.y += move_y

        if keys[pygame.K_SPACE]:
            self.boosting = True
            if not self.boost_sound_played:
                self.boost_sound.play()
                self.boost_sound_played = True
            if not self.fire_sound_played:
                self.fire_sound.play(-1)
                self.fire_sound_played = True
            if not self.boost_sound.get_num_channels():
                if not self.wind_noise_played:
                    self.wind_noise.play(-1)
                    self.wind_noise_played = True
        else:
            self.boosting = False
            self.boost_sound_played = False
            self.fire_sound_played = False
            self.wind_noise_played = False
            self.fire_sound.stop()
            self.boost_sound.fadeout(500)
            self.wind_noise.fadeout(500)

        # Update Sonic's position and collision rectangle
        self.rect.x = self.x
        self.rect.y = self.y

        # Update animation and direction
        self.update_animation()


    def update_animation(self):
        # Calculate animation speed based on Sonic's ground speed
        self.animation_speed = 0.1

        # Update the animation frame based on the animation speed
        self.frame += self.animation_speed

        # If the frame value exceeds the total number of frames, reset it to 0
        if self.frame >= len(self.idle_images):
            self.frame = 0

        # Determine the image index based on the current frame
        self.image_index = int(self.frame) % len(self.idle_images)
        if self.current_speed == 0:
            self.image = self.idle_images[self.image_index]
        elif self.direction == 1 and not self.boosting:
            self.image = self.fly_images[self.image_index]
            self.mask = pygame.mask.from_surface(self.image)
        elif self.direction == -1 and not self.boosting:
            self.image = pygame.transform.flip(self.fly_images[self.image_index], True, False)
            self.mask = pygame.mask.from_surface(self.image)
        elif self.direction == 1 and self.boosting:
            self.img = self.boosting_images[self.image_index]
            self.image = pygame.transform.rotate(self.img, 270)
            self.mask = pygame.mask.from_surface(self.image)
        elif self.direction == -1 and self.boosting:
            self.img = pygame.transform.flip(self.boosting_images[self.image_index], True, False)
            self.image = pygame.transform.rotate(self.img, 90)
            self.mask = pygame.mask.from_surface(self.image)

class E102Gamma(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.idle_images = [pygame.image.load(os.path.join("assets", "sprites", "Gamma", f"gammaidle{i}.png")).convert_alpha() for i in range (1, 9)]
        self.weapon_draw_images = [pygame.image.load(os.path.join("assets", "sprites", "Gamma", f"gammadrawgun{i}.png")).convert_alpha() for i in range (1, 9)]
        self.punching_images = [pygame.image.load(os.path.join("assets", "sprites", "Gamma", f"gammapunch{i}.png")).convert_alpha() for i in range (1, 9)]
        self.image = self.idle_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 5000  # Boss health
        self.max_health = 5000
        self.attack_interval = 3000  # Time between attacks in milliseconds
        self.last_attack_time = 0  # Timestamp of the last attack
        self.bullet_group = pygame.sprite.Group()  # Group to hold bullets
        self.frame = 0
        self.animation_speed = 0.1
        self.shooting = False
        self.punching = False
        self.weapon_drawn = False
        self.next_fire_time = 0
        self.laser_speed = 33
        self.hit_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "Hit.mp3"))
        self.laser_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "laser.mp3"))
        self.punch_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "swing.mp3"))
        self.explosion_images = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "Badniks", f"explosion{i}.png")).convert_alpha(), (self.rect.width, self.rect.height)) for i in range(1, 18)]
        self.punch_sound_played = False
        self.taken_hit = False
        self.laser_sound_played = False
        self.mask = pygame.mask.from_surface(self.image)
        self.defeated = False

    def attack(self):
        # Determine if it's time to attack
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= self.attack_interval:
            # Launch a barrage of bullets towards Sonic's current position
            # You can create a pattern of bullet firing based on your preference
            self.last_attack_time = current_time
            self.shooting = True
            self.launch_bullets()

    def punch_attack(self, sonic):
        # Start the punch attack
        self.punching = True
        self.shooting = False
        
        # Random chance of performing a punch attack
        if random.choice([0, 1]) == 1:
            frame = 0
            knockback_force = 1500  # Adjust as needed
            
            # Check for collision between the boss and Sonic
            if pygame.sprite.collide_mask(sonic, self):
                # Move Sonic away from the boss based on knockback force
                if sonic.rect.x > self.rect.x:
                    sonic.x += knockback_force  # Sonic is on the right of the boss
                else:
                    sonic.x -= knockback_force  # Sonic is on the left of the boss
                
                # Play punch sound if not already played
                if not self.punch_sound_played:
                    self.punch_sound.play()
                    self.punch_sound_played = True
            
            # Update the image frame for the punch attack animation
            frame += self.animation_speed
            if frame >= len(self.punching_images):
                frame = 0
            image_index = int(frame) % len(self.idle_images)
            # Update the current image of the boss during punch attack
            self.image = self.punching_images[image_index]
            self.rect = self.image.get_rect(center=self.rect.center)
            if self.image == self.punching_images[-2]:
                if not self.punch_sound_played:
                    self.punch_sound.play()
                    self.punch_sound_played = True
            # Check if the current image is the last image in the punching_images list
            if self.image == self.punching_images[-1]:
                # Reset punching and sound play flag
                self.punching = False
                self.punch_sound_played = False

    def launch_bullets(self):
        current_time = pygame.time.get_ticks()  # Use pygame.time.get_ticks() instead of time.time()
        if current_time >= self.next_fire_time:
            # Set the next fire time to the current time + 50 milliseconds (0.05 seconds)
            self.next_fire_time = current_time + 50  # Adjust the interval as needed (50 milliseconds)
            # Calculate a random starting Y position for the laser
            random_start_y = random.randint(self.rect.top, self.rect.bottom)
            # Instantiate a new laser at the random Y position with speed
            laser = Laser(self.rect.centerx, random_start_y, self.laser_speed, lifespan=5)
            if not self.laser_sound_played:
                self.laser_sound.play()
                self.laser_sound_played = True
            # Add the laser to the sprite group
            self.bullet_group.add(laser)
        self.laser_sound_played = False
        # Update the lasers
        self.bullet_group.update()
        if len(self.bullet_group) >= 50:
            self.shooting = False

    def update(self, sonic):
        if self.health <= 0:
            self.defeated = True
        # Calculate animation speed based on Sonic's ground speed
        self.animation_speed = 0.1
        self.bullet_group.update()
        # Update the animation frame based on the animation speed
        self.frame += self.animation_speed

        # If the frame value exceeds the total number of frames, reset it to 0
        if self.frame >= len(self.idle_images):
            self.frame = 0

        # Determine the image index based on the current frame
        self.image_index = int(self.frame) % len(self.idle_images)

        # Handle different states of the boss
        if not self.shooting:
            self.image = self.idle_images[self.image_index]
            self.mask = pygame.mask.from_surface(self.image)
        elif self.shooting and not self.weapon_drawn:
            self.image = self.weapon_draw_images[self.image_index]
            self.mask = pygame.mask.from_surface(self.image)
            if self.image == self.weapon_draw_images[7]:
                self.weapon_drawn = True
        elif self.shooting and self.weapon_drawn:
            self.image = self.weapon_draw_images[7]
            self.mask = pygame.mask.from_surface(self.image)
        elif self.punching:
            pass
        elif self.defeated:
            # If health is 0 or less, play the explosion animation
            self.image = self.explosion_images[self.image_index]
            # Update the frame for the explosion animation
            self.frame += self.animation_speed
            
            # If the explosion animation finishes, remove the boss
            if self.frame >= len(self.explosion_images):
                self.kill()
    
        # Handle collisions with Sonic
        if pygame.sprite.collide_mask(sonic, self):
            # Check if Sonic is boosting
            if sonic.boosting:
                # Random chance of the boss blocking the attack
                if random.random() < 0.1:  # 10% chance to block
                    # Blocked, no damage dealt
                    sonic.taken_hit = True
                    sonic.rect.x -= 100  # Flung back
                else:
                    if not self.taken_hit:
                        self.hit_sound.play()
                        self.health -= 10  # Deal 10 damage
                        sonic.immobile = True
                        sonic.rect.x -= 100  # Flung back
            # Handle bullet collisions (if any)
            # Decrease Sonic's health on bullet collision
            pass
        self.taken_hit = False