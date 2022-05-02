#imports necessary libraries
import pygame

#import random for random numbers
import random

#importing Local Variables such as keystokes instead of calling from pygame each time
from pygame.locals import(
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

#Creating a sprite player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.Surface((75, 25))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect()

	def update(self, pressed_keys):
		#move_ip() moves in place of rect in (x,y) coordinates
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
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
		
#Creating a new Sprite for Enemies
class Enemies(pygame.sprite.Sprite):
	#Setting up Sprite Surface and Rect
	def __init__(self):
		super(Enemies,self).__init__()
		self.surf = pygame.Surface((20,10))
		self.surf.fill((255,255,255))
		self.rect = self.surf.get_rect()		

	#Setting up a tuple for position of enemies in Screen
	center = (
		#Random number between width + 20 and Width + 100 is taken
		random.randint(SCREEN_WIDTH + 20,SCREEN_WIDTH + 100),
		#Random position at any height of screen
		random.randint(0,SCREEN_HEIGHT)
		)

	#Setting up speed of enemy between 5 to 20
	self.speed = random.randint(5,20)

	#moving sprite acc to speed
	def update(self):
		self.rect.move_ip(self.speed,0)
		if self.rect.right < 0:
			self.kill()

#Instantiate player otherwise its just a rect object
player =  Player()


#Defining constants for screen height and width
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

#Setting object for display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Initialize pygame
pygame.init()

#Variable to keep ,ain game loop running
run = True

#Main game loop
while run:
	#To handle every event
	for event in pygame.event.get():
		#is the event type a keystroke,KEYDOWN must be imported just like QUIT
		if event.type == KEYDOWN:
			#is the key ESC
			if event.key == K_ESCAPE:
				run = False
		#is the event type window closure
		elif event.type == QUIT:
			run = False 
	
	#Pressed Key Dictionary
	pressed_keys = pygame.key.get_pressed()

	#Calling player movement for pressed keys
	player.update(pressed_keys)


	#Fill screen with black
	screen.fill((0,0,0))
	
	#Draws 'Player' in the middle of screen and updates it
	#(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	screen.blit(player.surf,player.rect)

	#Update the display
	pygame.display.flip()