import sys
import pygame

#———————————————————————————————————————————————————————————————————————————————
#———————————————————————————————————————————————————————————————————————————————
class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	########################################
	def __init__(self):
		"""Initialize the game, and create game resources."""

		pygame.init()		# initialize Pygame background settings

		self.screen = pygame.display.set_mode((1200, 800))	# create display window (surface) &
															# assign to class attribute 'self.screen'
															# surface display.set_mode() returns is entire game window
		pygame.display.set_caption("Alien Invasion")

	########################################
	def run_game(self):
		"""Start the main loop for the game."""

		while True:
			# Watch for keyboard and mouse events,
			# which are any action user performs while playing the game
			# listen for events & perform task based on event
			for event in pygame.event.get():	# pygame.event.get() returns list of events that have
												# taken place since last time this function was called
				if event.type == pygame.QUIT:	# player clicked window's close button, detect pygame.QUIT event
					sys.exit()					# exit the game

			# Make the most recently drawn screen visible.
			# Update display to show new positions of game elements & hide
			# old ones, creating illusion of smooth movement
			pygame.display.flip()

#———————————————————————————————————————————————————————————————————————————————
#———————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
	ai = AlienInvasion()	# create instance of game
	ai.run_game()			# run game