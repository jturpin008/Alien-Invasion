import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	# param: self reference
	# param: reference to current instance of AlienInvasion class
	#		 to give Alien access to all resources defined in AlienInvasion
	########################################
	def __init__(self, aiGame):
		"""Initialize the alien & set its starting position."""

		super().__init__()				# call init() from parent class Sprite, granting child class Alien
										# access to all resources defined in Sprite
		self.screen = aiGame.screen		# assign game's screen attribute to Alien's screen attribute
		self.settings = aiGame.settings	# assign game's settings attribute to Alien's settings attribute

		# load the alien image & set its rect attribute
		self.image = pygame.image.load('images/alien.bmp')	# assign image returned by load() to Alien's image attribute
		self.rect = self.image.get_rect()					# assign surface rect returned by get_rect() to Aliein's rect attribute

		# start each new alien near the top left of the screen
		self.rect.x = self.rect.width		# set alien's rect's x-coordinate 1 Alien width away from initial placement (x-origin)
		self.rect.y = self.rect.height		# set alien's rect's y-coordinate 1 Alien height away from initial placement (y-origin)

		self.x = float(self.rect.x)			# cast Alien's rect's x-coordinate with float() to get its exact horizontal position &
											# assign it to Alien's exact(decimal) x-coordinate attribute

	########################################
	def check_edges(self):
		"""Return True if an alien is at edge of screen."""

		screenRect = self.screen.get_rect()		# assign game's screen rect attribute to variable 'screenRect'

		# if alien's rectangle's right edge attribute is greater than or equal to the right attribute of the screen's rect OR
		# if alien's rectangle's left edge attribute is less than or equal to 0
		if (self.rect.right >= screenRect.right) or (self.rect.left <= 0):
			return True;

	########################################
	def update(self):
		"""Move the alien to the right."""
		
		self.x += (self.settings.alienSpeed * self.settings.fleetDirection)	# multiply alien's speed by value of fleetDirection
																			# if fleetDirection is 1, value of alienSpeed added to alien's current position, moving it right
																			# if fleedDirection is -1, value of alienSpeed subtracted from alien's position, moving it left
		self.rect.x = self.x				# assign Alien's exact(decimal) x-coordinate attribute to Alien's rect's x-coordinate attribute