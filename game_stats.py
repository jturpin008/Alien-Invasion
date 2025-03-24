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
		#self.highScore = 0
		self.highScoreFile = 'high_score.txt'
		self.read_high_score(self.highScoreFile)

	########################################
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		
		self.shipsLeft = self.settings.shipLimit
		self.score = 0
		self.level = 1

	########################################
	def read_high_score(self, fileName=''):
		"""Open the file with the saved high score."""

		# open file in write mode, read it, & store as one long string
		with open(fileName, 'r') as fileObject:
			contents = fileObject.read()		# read file contents as one string

		if contents != '':
			self.highScore = int(contents)
			print(f"High score: {self.highScore}")
		else:
			print("High score file empty")
			self.highScore = 0