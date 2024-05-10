import pygame

class Ship:
	"""A class to manage the ship."""

	# 'Ship' takes 2 parameters: self reference &
	# reference to current instance of AlienInvasion class
	# This gives 'Ship' access to all game resources defined in AlienInvasion
	########################################
	def __init__(self, aiGame):
		"""Initialize the ship and set its starting position."""

		self.screen = aiGame.screen					# assign game's screen attribute to Ship's screen attribute
													# to easily access game's screen in all Ship class methods
		self.settings = aiGame.settings				# assign game's settings attribute to Ship's settings attribute
		self.screenRect = aiGame.screen.get_rect()	# assign game's screen rect attribute to Ship's screen rect attribute
													# to correctly place Ship in correct location on screen

		# load the shop image & get its rect
		self.image = pygame.image.load('images/ship.bmp')	# load() returns a surface representing the ship
															# assign returned surface to Ship's image attribute
		self.rect = self.image.get_rect()					# when image loaded, call get_rect() to access
															# Ship surface's rect attribute to use later to place the Ship

		# start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screenRect.midbottom		# match value of screen rect's midbottom attribute
															# to Ship screen rect's midbottom attribute

		# Because we're adjusting the position of the Ship by fractions of a pixel, we need to assign the position to a variable
		# that can store a decimal value. A decimal value assigned to rect will only keep the integer portion of the value.
		# To accurately track Ship's position, define a self.x attribute that can hold decimal values
		# Use float() to convert the value of self.rect.x to a decimal and assign this value to self.x
		self.x = float(self.rect.x)	# store a decimal value for the Ship's horizontal position

		self.movingRight = False	# initialize movingRight attribute(flag) to false
		self.movingLeft = False		# initialize movingLeft attribute(flag) to false

	# update() called through instance of Ship, so it's not considered a helper method
	# Using 2 separate if blocks rather than an elif allows Ship's rect.x value to be increased & then decreased when both
	# arrow keys are held down. This results in the Ship standing still.
	# elif for motion to the the left would cause the right arrow key to have priority. This makes movements more accurate
	# when switching from right to left when the player might momentarily hold down both keys.
	########################################
	def update(self):
		"""Update the ship's position based on the movement flags."""

		# update Ship's x position value
		if self.movingRight:					# if movingRight flag set to true
			self.x += self.settings.shipSpeed	# adjust x position by value of (+)shipSpeed
		if self.movingLeft:						# if movingLeft flag set to true
			self.x -= self.settings.shipSpeed	# adjust x position by value of (-)shipSpeed

		self.rect.x = self.x					# update Ship's rect.x value with updated self.x value
												# only integer portion of self.x will be stored in self.rect.x, that's acceptable

	########################################
	def blitme(self):
		"""Draw the ship at its current location."""

		self.screen.blit(self.image, self.rect)