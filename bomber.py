#!/usr/bin/env python

import random
import sys

import pygame

from gamelib.viewer import Viewer
from gamelib.loader import Loader
from gamelib import sprites


class MyGame(Viewer):

	def __init__(self):
		Viewer.__init__(self)
		self.draw_func = self.draw
		self.event_func = self.process_events
		self.buildings = []
		self.in_menu = True

		for i in xrange(0,10):
			self.buildings.append(pygame.sprite.Group())
		self.explosions = pygame.sprite.Group()
		self.bombs = pygame.sprite.Group()

	def load_rsc(self):
		self.bkg = Loader.load_pixmap("rsc/fondo.png")
		self.bkg_rect = self.bkg.get_rect()
		self.menu = Loader.load_png("rsc/main.png")
		self.menu_rect = self.menu.get_rect()
		self.end = Loader.load_png("rsc/end.png")
		self.end_rect = self.end.get_rect()

		self.exp_sound = Loader.load_sound("rsc/explosion.wav")
		self.exp_sound.set_volume(0.15)
		pygame.mixer.music.load("rsc/bkg.wav")
		pygame.mixer.music.set_volume(0.2)
		pygame.mixer.music.play(-1)

		self.plane = sprites.Plane()
		self.plane.init()

	def init_game(self):
		self.explosions.empty()
		self.bombs.empty()

		self.create_map()
		self.plane.init_pos()
		self.alive = True
		self.in_menu = False
		self.in_final_screen = False

	def create_map(self):
		for i, group in enumerate(self.buildings):
			group.empty()
			base = sprites.Base()

			key = "ORANGE"
			if random.randint(0,2) == 0:
				key = ("YELOW")
			
			base.init(key)
			base_width = base.rect.width
			base_height = base.rect.height
			base.rect.move_ip(base_width * i, MyGame.Height - base_height - 10)
			group.add(base)

			h = random.randint(1,8)
			for j in xrange(0,h):
				floor = sprites.Floor()
				floor.init(key)
				floor.rect.move_ip(base_width*i, 490 - base_height*j)
				group.add(floor)


	def check_collisions(self):
		y = self.plane.rect.centerx
		for group in self.buildings:
			c = pygame.sprite.spritecollide(self.plane, group, True)
			if c:
				exp = sprites.Explosion()
				exp.init()
				exp.rect.left = self.plane.rect.left - 10
				exp.rect.top = self.plane.rect.top - 25
				self.explosions.add(exp)
				self.alive = False
				self.exp_sound.play()
			for bomb in self.bombs:
				c = pygame.sprite.spritecollide(bomb, group, True)
				if c:
					exp = sprites.Explosion()
					exp.init()
					exp.rect.centerx = c[0].rect.centerx
					exp.rect.centery = c[0].rect.centery
					self.explosions.add(exp)
					bomb.kill()
					self.exp_sound.play()

	def draw(self, time_passed):
		self.screen.blit(self.bkg, self.bkg_rect)
		if self.in_menu:
			self.draw_menu()
		elif self.in_final_screen:
			self.draw_end()
		else:
			self.draw_game(time_passed)

	def draw_menu(self):
		self.screen.blit(self.menu, self.menu_rect)
			
	def draw_end(self):
		self.screen.blit(self.end, self.end_rect)

	def draw_game(self, time_passed):
		self.check_collisions()
		for group in self.buildings:
			group.draw(self.screen)
		self.explosions.update(time_passed)
		self.explosions.draw(self.screen)
		self.bombs.update(time_passed)
		self.bombs.draw(self.screen)

		if self.alive:
			self.plane.update(time_passed)
			self.screen.blit(self.plane.image, self.plane.rect)
		else:
			self.in_menu = not self.explosions

		isend = map(lambda x: len(x) == 0, self.buildings)
		self.in_final_screen = False not in isend

	def add_bomb(self):
		if not self.bombs and self.alive:
			bomb = sprites.Bomb()
			bomb.init(self.plane.rect.centerx,self.plane.rect.bottom)
			self.bombs.add(bomb)

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)

			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				if self.in_menu or self.in_final_screen:
					self.init_game()
				else:
					self.add_bomb()
		
def main():
	pygame.init()

	game = MyGame()
	game.init_windowed((800,600), "Crazy Bomber")
	game.load_rsc()
	game.main_loop()

if __name__ == "__main__":
	main()
