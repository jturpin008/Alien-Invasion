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

	########################################
	def blitme(self):
		"""Draw the ship at its current location."""

		self.screen.blit(self.image, self.rect)