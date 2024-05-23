import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

#———————————————————————————————————————————————————————————————————————————————
#———————————————————————————————————————————————————————————————————————————————
class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	########################################
	def __init__(self):
		"""Initialize the game, and create game resources."""

		pygame.init()				# initialize all imported Pygame modules
		self.settings = Settings()	# create instance of Settings & assign it to 'self.settings'

		
		# settings to display game in its own window rather than fullscreen
		self.screen = pygame.display.set_mode(
			(self.settings.screenWidth, self.settings.screenHeight))	# create display window (surface) &
																		# assign to class attribute 'self.screen'
																		# surface display.set_mode() returns is entire game window
		

		"""
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)	# tell Pygame to figure out a window size & fill the screen
																			# because we don't know screen width & height ahead of time,
																			# update these settings after screen is created
		"""
		self.settings.screenWidth = self.screen.get_rect().width			# use width attribute of screen's rect to update settings object
		self.settings.screenHeight = self.screen.get_rect().height			# use height attribute of screen's rect to update settings object

		pygame.display.set_caption("Alien Invasion")

		self.bgColor = (self.settings.bgColor)	# set background color
		self.ship = Ship(self)					# Make instance of Ship after screen has been created
												# passing instance of AlienInvasion as an argument.
												# This parameter gives Ship access to game's resources like the screen object.
												# Assign this Ship instance to AlienInvasion's ship attribute.
		self.grpBullets = pygame.sprite.Group()	# create sprite group to store, manage, & draw all live bullets fired
												# Group() behaves like a list with extra functionality

	########################################
	def run_game(self):
		"""Start the main loop for the game."""

		while True:
			self._check_events()			# check for & respond to keyboard & mouse events
			self.ship.update()				# update ship's position on current pass through loop
			self.grpBullets.update()		# grpBullets.update() calls bullet.update() for each bullet placed in group 'grpBullets'
			self._update_screen()			# update images on screen & flip to newly updated screen
			
	########################################
	def _check_events(self):
		"""Helper method to respond to keypresses & mouse events."""

		# Watch for keyboard & mouse events,
		# which are any action user performs while playing the game
		# listen for events & perform task based on event
		for event in pygame.event.get():			# pygame.event.get() returns list of events that have
													# taken place since last time this function was called
			if event.type == pygame.QUIT:			# player clicked window's close button, detect pygame.QUIT event
				sys.exit()							# exit the game
			
			elif event.type == pygame.KEYDOWN:		# player pressed a key: pygame catches KEYDOWN event
				self._check_keydown_events(event)	# handle the key press event
			
			elif event.type == pygame.KEYUP:		# player released a pressed key: pygame catches KEYUP event
				self._check_keyup_events(event)		# handle the key release event

	########################################
	def _check_keydown_events(self, event):
		"""Helper method to respond to keypresses."""

		if event.key == pygame.K_RIGHT:		# if player pressed right arrow key
			self.ship.movingRight = True	# set ship's movingRight flag to true

		elif event.key == pygame.K_LEFT:	# if player pressed left arrow key
			self.ship.movingLeft = True		# set ship's movingLeft flag to true

		elif event.key == pygame.K_q:		# if player pressed 'q' key
			sys.exit()						# exit the game

		elif event.key == pygame.K_SPACE:	# if player pressed space bar
			self._fire_bullet()				# fire the bullet from the ship

	########################################
	def _check_keyup_events(self, event):
		"""Helper method to respond to key releases."""

		if event.key == pygame.K_RIGHT:		# if player released right arrow key
			self.ship.movingRight = False	# set ship's movingRight flag to False

		elif event.key == pygame.K_LEFT:	# if player released left arrow key
			self.ship.movingLeft = False	# set ship's movingLeft flag to false

	########################################
	def _fire_bullet(self):
		"""Helper method to create a new bullet and add it to the bullets group."""

		newBullet = Bullet(self)		# create instance of a bullet
		self.grpBullets.add(newBullet)	# add newly created bullet to group 'grpBullets'
										# add() similar to append but written for Pygame groups

	########################################
	def _update_screen(self):
		"""Helper method to update images on the screen, & flip to the new screen."""

		self.screen.fill(self.bgColor)	# redraw screen during each pass through loop
		self.ship.blitme()				# After filling background, place image of ship
										# on top of background.

		for bullet in self.grpBullets.sprites():	# iterate through each bullet in the group(list) 'grpBullets'
			bullet.draw_bullet()					# draw the bullet to the screen

		# Make the most recently drawn screen visible.
		# Update display to show new positions of game elements & hide
		# old ones, creating illusion of smooth movement
		pygame.display.flip()

#———————————————————————————————————————————————————————————————————————————————
#———————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
	ai = AlienInvasion()	# create instance of game
	ai.run_game()			# run game