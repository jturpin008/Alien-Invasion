class GameStats:
	"""Track statistics for Alien Invasion."""

	########################################
	def __init__(self, aiGame):
		"""Initialize statistics."""
		self.settings = aiGame.settings		# assign game's settings to GameStats' settings attribute
		self.reset_stats()

		# start Alien Invasion in an inactive state
		self.gameActive = False

		# high score should never be reset
		self.highScore = 0

	########################################
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		
		self.shipsLeft = self.settings.shipLimit
		self.score = 0