import pygame

from viewer import Viewer
from loader import Loader

class Base(pygame.sprite.Sprite):
	images = {}

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

	def init(self, type):
		if not Base.images:
			Base.images = {
				"YELOW" : Loader.load_pixmap("rsc/base1.png"),
				"ORANGE" : Loader.load_pixmap("rsc/base2.png")
			 	}

		self.image = Base.images[type]
		self.rect = self.image.get_rect()

class Floor(pygame.sprite.Sprite):
	images = {}

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

	def init(self, type):
		if not Floor.images:
			Floor.images = {
				"YELOW" : Loader.load_pixmap("rsc/floor1.png"),
				"ORANGE" : Loader.load_pixmap("rsc/floor2.png")
			 	}
		self.image = Floor.images[type]
		self.rect = self.image.get_rect()

class Plane(pygame.sprite.Sprite):
	images = []

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.velocity = -0.25

	def init(self):
		if not Plane.images:
			Plane.images = [
				Loader.load_png("rsc/plane1.png"),
				Loader.load_png("rsc/plane2.png"),
				Loader.load_png("rsc/plane3.png")
				]
		self.image_ind = 0
		self.rect = Plane.images[0].get_rect()
		self.image = Plane.images[0]
		self.playing_time = 0

	def init_pos(self):
		self.rect.left = Viewer.Width - self.rect.width
		self.rect.top = 40

	def update(self, time_passed):
		xoff = round(self.velocity * time_passed)
		self.rect.move_ip(xoff,0)
		if self.rect.left < -self.rect.width:
			self.rect.left = Viewer.Width
			self.rect.top += self.rect.height

		self.image_ind = (self.playing_time / 150) % 3
		self.image = Plane.images[self.image_ind]
		self.playing_time += time_passed


class Explosion(pygame.sprite.Sprite):
	images = []

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

	def init(self):
		if not Explosion.images:
			Explosion.images = [
				Loader.load_png("rsc/exp1.png"),
				Loader.load_png("rsc/exp2.png"),
				Loader.load_png("rsc/exp3.png"),
				Loader.load_png("rsc/exp4.png"),
				Loader.load_png("rsc/exp5.png")
				]
		self.image_ind = 0
		self.rect = Explosion.images[0].get_rect()
		self.image = Explosion.images[0]
		self.playing_time = 0


	def update(self, time_passed):
		self.image_ind = self.playing_time / 150
		self.playing_time += time_passed
		try:
			self.image = Explosion.images[self.image_ind]
		except IndexError:
			self.kill()

class Bomb(pygame.sprite.Sprite):
	image = None

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.velocity = 0.25

	def init(self, x, y):
		if not Bomb.image:
			Bomb.image = Loader.load_png("rsc/bomb.png")
		self.image = Bomb.image
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y

	def update(self, time_passed):
		yoff = round(time_passed * self.velocity)
		self.rect.top += yoff

		if self.rect.top > Viewer.Height - 10:
			self.kill()
