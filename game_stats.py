class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, aiGame):
		"""Initialize statistics."""
		self.settings = aiGame.settings		# assign game's settings to GameStats' settings attribute
		self.reset_stats()

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.shipsLeft = self.settings.shipLimit