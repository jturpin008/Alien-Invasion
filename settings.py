class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""

		# screen settings
		self.screenWidth = 1200
		self.screenHeight = 800
		self.bgColor = (230, 230, 230)

		# Ship settings
		self.shipSpeed = 1.5		# Ship's initial speed in pixels/loop

		# bullet settings
		self.bulletSpeed = 1.0
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletColor = (60, 60, 60)
		self.bulletsAllowed = 3