import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
			(self.settings.screenWidth, self.settings.screenHeight))		# initialize game's display window & assign to AlienInvasion's screen attribute
		

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
		self.grpAliens = pygame.sprite.Group()	# create sprite group to store, manage, & draw all aliens
		self._create_fleet()					# create the fleet of aliens

	########################################
	def run_game(self):
		"""Start the main loop for the game."""

		while True:
			self._check_events()		# check for & respond to keyboard & mouse events
			self.ship.update()			# update ship's position on current pass through loop
			self._update_bullets()		# update position of current bullets & delete old bullets
			self._update_aliens()		# update the positions of all aliens in the fleet
			self._update_screen()		# update images on screen & flip to newly updated screen
			
	########################################
	def _check_events(self):
		"""Helper method to respond to keypresses & mouse events."""

		# Listen for keyboard and/or mouse events & respond accordingly
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
	def _create_fleet(self):
		"""Create the fleet of aliens."""

		# create an alien & find the number of aliens in a row
		# spacing between each alien is equal to one alien width.

		alien = Alien(self)							# create new instance of Alien for testing purposes
		alienWidth, alienHeight = alien.rect.size	# define width & height of an alien
													# rect.size returns tuple with width & height of a rect object
		availableSpaceX = self.settings.screenWidth - (2 * alienWidth)	# horizontal space available for alien fleet
																		# subtract width of 2 aliens, 1 on either side
		numberAliensX = availableSpaceX // (2 * alienWidth)		# to determine how many alien ships can fit in the horizontal space available
																# divide available x-axis by width of 2 alien ships (discarding any remainder)
																# 2 alien ships because empty space between alien ships equals width of 1 alien ship

		# determine number of rows of aliens that fit on the screen
		shipHeight = self.ship.rect.height					# define the height of the ship
		availableSpaceY = (self.settings.screenHeight -
			(3 * alienHeight) - shipHeight)					# from the height of the entire screen:
															# subtract 1 alien height from top of screen
															# subtract 1 ship height from bottom of screen
															# subtract 2 more alien heights from bottom of screen
		
		numberRows = availableSpaceY // (2 * alienHeight)	# because we're dividing available space by the height of the aliens
															# multiplying alien height by 2 cuts the number of rows in half, just as
															# multiplying by 3 would cut the number of rows to 1/3
															# use floor division because we can only make integer number of rows

		# create the full fleet of aliens
		for rowNumber in range(numberRows):					# iterate through each row of aliens that can be created in the vertical space available
			for alienNumber in range(numberAliensX):		# iterate through each alien that can be created in the horizontal space available in the current row
				self._create_alien(alienNumber, rowNumber)	# create an alien & place it in the row

	# param: self reference
	# param: alien's position from left to right within the current row
	# param: row on which to place the alien
	########################################
	def _create_alien(self, alienNumber, rowNumber):
		"""Create an alien & place it in the row."""

		alien = Alien(self)								# create new instance of Alien
		alienWidth, alienHeight = alien.rect.size		# define width & height of an alien
														# rect.size returns tuple with width & height of a rect object
		alien.x = alienWidth + ((2 * alienWidth) * alienNumber)	# place current alien to the right one alien width from the left margin
																# plus the width of an alien multiplied by 2 to account for the alien & the space to its right, also the width of an alien
																# multiply all this by the alien's position in the row

		alien.rect.x = alien.x		# assign alien ship's x-coordinate value to its rect.x value
									# integer value will be stored, decimal value will be lost, that's ok for now

		alien.rect.y = (alien.rect.height +
			((2 * alien.rect.height) * rowNumber))	# pad empty upper border by a height of 1 alien rect
													# plus the height of 1 alien & the empty space below it also the height of 1 alien
													# multiplied by the current row number

		self.grpAliens.add(alien)	# add newly created alien to grpAliens


	########################################
	def _fire_bullet(self):
		"""Helper method to create a new bullet and add it to the bullets group."""

		# if bullet count visible on screen is less than quantity desired
		if len(self.grpBullets) < self.settings.bulletsAllowed:
			newBullet = Bullet(self)		# create instance of a bullet
			self.grpBullets.add(newBullet)	# add newly created bullet to group 'grpBullets'
											# add() similar to append but written for Pygame groups

	########################################
	def _update_bullets(self):
		"""Helper method to update position of bullets & get rid of old bullets."""

		# update bullet positions.
		self.grpBullets.update()		# grpBullets.update() calls bullet.update() for each bullet placed in group 'grpBullets'

		# get rid of bullets that have disappeared
		for bullet in self.grpBullets.copy():	# can't remove items from group(list) within a for loop, loop through copy of 'grpBullets'group
												# iterate through each item in copy of 'grpBullets' group
			if bullet.rect.bottom <= 0:			# if bottom of current bullet's rect is no longer on the screen
				self.grpBullets.remove(bullet)	# remove current bullet from original 'grpBullets' group
		#print(len(self.grpBullets))			# print how many bullets remaining

	########################################
	def _update_aliens(self):
		"""Helper method to update the positions of all aliens in the fleet."""

		self.grpAliens.update()	# update the positions of all aliens in the fleet

	########################################
	def _update_screen(self):
		"""Helper method to update images on the screen, & flip to the new screen."""

		self.screen.fill(self.bgColor)	# redraw screen during each pass through loop
		self.ship.blitme()				# After filling background, place image of ship
										# on top of background.

		for bullet in self.grpBullets.sprites():	# iterate through each bullet in the group(list) 'grpBullets'
			bullet.draw_bullet()					# draw the bullet to the screen

		self.grpAliens.draw(self.screen)			# draw sprite(s) in grpAliens group to the screen
													# at respective position(s) defined by rect attribute(s)

		# Make the most recently drawn screen visible.
		# Update display to show new positions of game elements & hide
		# old ones, creating illusion of smooth movement
		pygame.display.flip()

#———————————————————————————————————————————————————————————————————————————————
#———————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
	ai = AlienInvasion()	# create instance of game
	ai.run_game()			# run game