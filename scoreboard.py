import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
	"""A class to report scoring information."""

	# • self reference
	# • reference to over all game class
	########################################
	def __init__(self, aiGame):
		"""Initialize scorekeeping attributes"""

		self.aiGame = aiGame
		self.screen = aiGame.screen
		self.screenRect = self.screen.get_rect()
		self.settings = aiGame.settings
		self.stats = aiGame.stats

		# font settings for scoring information
		self.textColor = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# prepare the initial score images
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

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
	def prep_high_score(self):
		"""Turn the high score into a rendered image."""

		highScore = round(self.stats.highScore, -1)	# round high score to nearest 10
		highScoreStr = "{:,}".format(highScore)		# format high score with commas
		
		self.highScoreImage = self.font.render(highScoreStr, True,
				self.textColor, self.settings.bgColor)

		# center the high score at the top of the screen
		self.highScoreRect = self.highScoreImage.get_rect()
		self.highScoreRect.centerx = self.screenRect.centerx
		self.highScoreRect.top = self.screenRect.top + 20

	########################################
	def prep_level(self):
		"""Turn the level into a rendered image."""

		levelStr = str(self.stats.level)
		self.levelImage = self.font.render(levelStr, True,
				self.textColor, self.settings.bgColor)

		# position othe level below the score
		self.levelRect = self.levelImage.get_rect()
		self.levelRect.right = self.scoreRect.right
		self.levelRect.top = self.scoreRect.bottom + 10

	########################################
	def prep_ships(self):
		"""Show how many ships are left."""

		self.grpShips = Group()		# empty group of self.ships

		for shipNumber in range(self.stats.shipsLeft):	# iterate through the player's remaining ships
			ship = Ship(self.aiGame)					# create new instance of a ship
			ship.rect.x = 10 + (shipNumber * ship.rect.width)
			ship.rect.y = 10
			self.grpShips.add(ship)						# add current ship to the group

	########################################
	def show_score(self):
		"""Draw scores, level, & ships to the screen."""

		self.screen.blit(self.scoreImage, self.scoreRect)
		self.screen.blit(self.highScoreImage, self.highScoreRect)
		self.screen.blit(self.levelImage, self.levelRect)
		self.grpShips.draw(self.screen)

	########################################
	def check_high_score(self):
		"""Check to see if there's a new high score."""

		if self.stats.score > self.stats.highScore:
			self.stats.highScore = self.stats.score
			self.prep_high_score()