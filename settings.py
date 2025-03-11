class Settings:
	"""A class to store all settings for Alien Invasion."""

	########################################
	def __init__(self):
		"""Initialize the game's static settings."""

		# screen settings
		self.screenWidth = 1200
		self.screenHeight = 800
		self.bgColor = (230, 230, 230)

		# Ship settings
		self.shipSpeed = 1.0		# Ship's initial speed in pixels/loop
		self.shipLimit = 3

		# bullet settings
		self.bulletSpeed = 1.0
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletColor = (60, 60, 60)
		self.bulletsAllowed = 3

		# alien settings
		self.alienSpeed = 0.2		# speed aliens move on x-axis
		self.fleetDropSpeed = 10	# speed fleet drops down screen each time an alien reaches either end
		self.fleetDirection = 1		# 1 == right; -1 == left

		# how quickly game speeds u p
		self.speedupScale = 1.5

		# how quickly the alien point values increas
		self.scoreScale = 1.5

		self.initialize_dynamic_settings()

	########################################
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""

		self.shipSpeed = 1.0
		self.bulletSpeed = 1.0
		self.alienSpeed = 0.2

		# fleetDirection of 1 represents right; -1 represents left
		self.fleetDirection = 1

		# scoring
		self.alienPoints = 50

	########################################
	def increase_speed(self):
		"""Increase speed settings & alien point values"""

		self.shipSpeed *= self.speedupScale
		self.bulletSpeed *= self.speedupScale
		self.alienSpeed *= self.speedupScale

		self.alienPoints = int(self.alienPoints * self.scoreScale)