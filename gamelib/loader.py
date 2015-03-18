
import pygame


class _NoneSound(object):
	def play(self):
		pass


class Loader(object):

	@staticmethod
	def load_pixmap(filename):
		try:
			image = pygame.image.load(filename).convert()
		except pygame.error, message:
			raise SystemExit, message
	
		return image

	@staticmethod
	def load_masked_pixmap(filename):
		image = load_solid_pixmap(filename)
		color = image.get_at((0, 0))
		image.set_colorkey(color, pygame.RLEACCEL)
		return image

	@staticmethod
	def load_png(filename):
		try:
			image = pygame.image.load(filename).convert_alpha()
		except pygame.error, message:
			raise SystemExit, message
	
		return image

	@staticmethod
	def load_font(filename, size):
		try:
			font = pygame.font.Font(filename, size)
		except pygame.error, message:
			raise SystemExit, message
	
		return font

	@staticmethod
	def load_sound(filename):
		if pygame.mixer is None:
			return _NoneSound()

		try:
			sound = pygame.mixer.Sound(filename)
		except pygame.error, message:
			raise SystemExit, message

		return sound

