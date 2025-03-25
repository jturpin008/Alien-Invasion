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

		contents = ''

		try:
			# open file in write mode, read it, & store as one long string
			with open(fileName, 'r') as fileObject:
				contents = fileObject.read()		# read file contents as one string
		except FileNotFoundError:
			# create file to store high score & assign 0 to high score
			with open(fileName, 'w') as fileObject:
				self.highScore = 0
				fileObject.write(str(self.highScore))

		if contents != '':
			self.highScore = int(contents)
		else:
			self.highScore = 0