import pygame.font

class Button:
	"""A Class to manage the play button."""

	########################################
	def __init__(self, aiGame, msg):
		"""Initialize button attributes"""

		self.screen = aiGame.screen					# assign game's screen surface attribute to Button's screen surface attribute
		self.screenRect = self.screen.get_rect()	# Button's screen's rectangular area

		# set dimensions & properties of the button
		self.width, self.height = 200, 50
		self.buttonColor = (0, 255, 0)
		self.textColor = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# build the button's rect object & center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screenRect.center

		# button message needs to be prepped only once
		self._prep_msg(msg)

	########################################
	def _prep_msg(self, msg):
		"""Turn msg into a rendered image & center text on the button"""

		self.msgImg = self.font.render(msg, True, self.textColor,
			self.buttonColor)										# turn text stored in msg into an image & store in msgImg
		self.msgImgRect = self.msgImg.get_rect()
		self.msgImgRect.center = self.rect.center

	########################################
	def draw_button(self):

		# draw blank button & then draw message
		self.screen.fill(self.buttonColor, self.rect)
		self.screen.blit(self.msgImg, self.msgImgRect)