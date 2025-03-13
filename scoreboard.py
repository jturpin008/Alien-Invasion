import pygame.font

class Scoreboard:
	"""A class to report scoring information."""

	# • self reference
	# • reference to over all game class
	########################################
	def __init__(self, aiGame):
		"""Initialize scorekeeping attributes"""

		self.screen = aiGame.screen
		self.screenRect = self.screen.get_rect()
		self.settings = aiGame.settings
		self.stats = aiGame.stats

		# font settings for scoring information
		self.textColor = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# prepare the initial score image
		self.prep_score()

	########################################
	def prep_score(self):
		"""Turn the score into a rendered image."""

		roundedScore = round(self.stats.score, -1)	# -1 rounds to nearest 10, -2 rounds to nearest 100... etc.
		scoreStr = "{:,}".format(roundedScore)		# insert commas into numbers when converting numerical value to string

		self.scoreImage = self.font.render(scoreStr, True,
				self.textColor, self.settings.bgColor)

		# display the score at the top right of the screen
		self.scoreRect = self.scoreImage.get_rect()
		self.scoreRect.right = self.screenRect.right - 20
		self.scoreRect.top = 20

	########################################
	def show_score(self):
		"""Draw score to the screen"""

		self.screen.blit(self.scoreImage, self.scoreRect)