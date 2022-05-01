#imports necessary libraries
import pygame

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
	
	#Fill screen with black
	screen.fill((0,0,0))
	
	#Draws 'Player' in the middle of screen and updates it
	#(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	screen.blit(player.surf,player.rect)

	#Update the display
	pygame.display.flip()