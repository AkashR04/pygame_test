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

#Defining constants for screen height and width
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

#Setting object for display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Part 4 - Drawing on a surface

#Filling screen the display variable with white by passing a tuple
screen.fill((255,255,255)) 

#Create a surface by adding tuple of width 50 amd length 50
surf = pygame.Surface((50,50))

surf.fill((0,0,0))
rect = surf.get_rect()
#Creating a variable to store center of surface
surf_center = (
		(SCREEN_WIDTH - surf.get_width()) / 2,
		(SCREEN_HEIGHT - surf.get_height()) / 2,
)
#Draws 'surf' in the middle of screen and updates it

screen.blit(surf,surf_center)
pygame.display.flip()


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
	