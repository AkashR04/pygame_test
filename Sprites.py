#imports necessary libraries
import sys
sys.path.insert(0, 'D:/Study/pypacka')

import pygame
import os
#import random for random numbers
import random


#importing Local Variables such as keystokes instead of calling from pygame each time
from pygame.locals import(
	RLEACCEL,
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)

#initialization of the game
pygame.init()

#Defining constants for screen height and width
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

#Setting object for display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Creating a sprite player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		#self.surf = pygame.Surface((75, 25))
		#self.surf.fill((255, 255, 255))
		#Using an image instead
		#file_name = os.path.join( 'Art', 'fighter.png')
		self.surf = pygame.image.load('Art/Fly.png').convert_alpha()
		self.surf.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.surf.get_rect()

	def update(self, pressed_keys):
		#move_ip() moves in place of rect in (x,y) coordinates
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
			move_up_sound.play()
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
			move_down_sound.play()
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)
		
		#To make sure player doesn't go off boundary
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH

		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT
		
#Custom event for adding an enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,250)

#Custom event for adding an cloud every second
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD,1000)

#Instantiate player otherwise its just a rect object
player =  Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
#Adding  a cloud sprite group
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Creating a new Sprite for Enemies
class Enemies(pygame.sprite.Sprite):
	#Setting up Sprite Surface and Rect
	def __init__(self):
		super(Enemies,self).__init__()
		#self.surf = pygame.Surface((20,10))
		#self.surf.fill((255,255,255))
		#Adding an image for enemy
		self.surf = pygame.image.load('Art/Bullet_1.png').convert_alpha()
		self.surf.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.surf.get_rect(
			#Setting up a tuple for position of enemies in Screen
			center = (
				#Random number between width + 20 and Width + 100 is taken
				random.randint(SCREEN_WIDTH + 10,SCREEN_WIDTH + 100),
				#Random position at any height of screen
				random.randint(0,SCREEN_HEIGHT)
			)
			)		

		

		#Setting up speed of enemy between 5 to 20
		self.speed = random.randint(5,20)

	#moving sprite acc to speed
	def update(self):
		self.rect.move_ip(-self.speed,0)
		if self.rect.right < 0:
			self.kill()

#Creating a new sprite for clouds
class Cloud(pygame.sprite.Sprite):
	def __init__(self):
		super(Cloud,self).__init__()
		#Adding an image for cloud
		self.surf = pygame.image.load('Art/nuvem.png').convert_alpha()
		#253,249
		self.surf.set_colorkey((0,0,0),RLEACCEL)
		# The starting position is randomly generated

		self.rect = self.surf.get_rect(

			center=(
					random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 50),
					random.randint(0, SCREEN_HEIGHT),
					)
			)

	#Cloud movement
	def update(self):
		self.rect.move_ip(-5, 0)
		if self.rect.right < 0:
			self.kill()





#Initialize pygame
pygame.init()

# Setup for sounds. Defaults are good.
pygame.mixer.init()

#Creating a game clock
clock =  pygame.time.Clock()

#Variable to keep ,ain game loop running
run = True

#Backgroud music
pygame.mixer.music.load('Sounds/bg.wav')
pygame.mixer.music.play(loops = -1)

#Movement sounds
move_up_sound = pygame.mixer.Sound('Sounds/s1.mp3')
move_down_sound = pygame.mixer.Sound('Sounds/s2.mp3')

#Collison sound
collison_sound = pygame.mixer.Sound('Sounds/s3.mp3')

#Main game loop
while run:
	#To handle every event
	for event in pygame.event.get():
		#is the event type a keystroke,KEYDOWN must be imported just like QUIT
		if event.type == KEYDOWN:
			#is the key ESC
			if event.key == K_ESCAPE:
				run = False
		
		#Handling ADDENEMY event
		elif event.type == ADDENEMY:
			new_enemy = Enemies()
			enemies.add(new_enemy)
			all_sprites.add(new_enemy)
		
		#Handling ADDCLOUD event
		elif event.type == ADDCLOUD:
			new_cloud = Cloud()
			clouds.add(new_cloud)
			all_sprites.add(new_cloud)
		
		#is the event type window closure
		elif event.type == QUIT:
			run = False 
	
	#Pressed Key Dictionary
	pressed_keys = pygame.key.get_pressed()
	#Calling defined cloud movement
	clouds.update()
	#Calling player movement for pressed keys
	player.update(pressed_keys)

	#Calling defined enemy movement
	enemies.update()
	
	
	#Fill screen with blue
	screen.fill((136,206,250))
	
	#Draws 'Player' in the middle of screen and updates it
	#(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	#screen.blit(player.surf,player.rect)
	# Draw all sprites
	for entity in all_sprites:
		screen.blit(entity.surf, entity.rect)

	#Collision detection for player
	if pygame.sprite.spritecollideany(player, enemies):
		#If collided remove player from group and stop game
		player.kill()
		move_up_sound.stop()
		move_down_sound.stop()
		collison_sound.play()
		#Stop game
		run = False

	#Game frome rate
	clock.tick(30)

	#Update the display
	pygame.display.flip()