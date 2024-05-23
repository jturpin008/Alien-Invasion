import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""

	# Note: when using sprites, you can group related elements in your game &
	# act on all the grouped elements at once

	# 2 parameters:
	#	• self reference
	#	• reference to current instance of AlienInvasion class
	#	  to give 'Bullet' access to all game resources defined in AlienInvasion
	########################################
	def __init__(self, aiGame):
		"""Create a bullet object at the ship's current position."""

		super().__init__()						# call init() from parent class Sprite, granting child class Bullet
												# access to all attributes defined in Sprite
		self.screen = aiGame.screen				# assign game's screen attribute to Bullet's screen attribute
		self.settings = aiGame.settings			# assign game's settings attribute to Bullet's settings attribute
		self.color = self.settings.bulletColor	# assign bullet color defined in Settings class to Bullet's color attribute

		# Bullet not based on an image, build a rect from scratch with Rect(),
		# then initialize at (0, 0) & set correct position based on the ship's positon
		self.rect = pygame.Rect(0, 0, self.settings.bulletWidth,
			self.settings.bulletHeight)				# create new Rect at (0, 0) of desired width & height & assign to Bullet's rect attribute
		self.rect.midtop = aiGame.ship.rect.midtop	# assign game's ship's rect's midtop attribute to Bullet's rect's midtop attribute
													# making it look like the bullet emerges from the top of the ship when it's fired

		self.y = float(self.rect.y)					# cast Bullet's rect's y-coordinate with float() to calculate a decimal value &
													# assign it to the Bullet's y-coordinate

	########################################
	def update(self):
		"""Move the bullet up the screen, corresponding to a decreasing y-coordinate."""

		# update the decimal position of the bullet
		self.y -= self.settings.bulletSpeed		# update bullet's y-coordinate by value of (-)bulletSpeed

		# update the rect position
		self.rect.y = self.y					# set Bullet's rect.y attribute to match value of Bullet's y-coordinate(self.y)

	########################################
	def draw_bullet(self):
		"""Draw the bullet to the screen."""

		pygame.draw.rect(self.screen, self.color, self.rect)	# draw the bullet