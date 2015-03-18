
""" Este modulo solo contiene una clase para crear una ventana simple con
pygame.

Para usar la clase basta con crear un objeto de la clase y llamar al metodo
init_windowed para crear la ventana y main_loop para entrar en el bucle
principal de la aplicacion.

Por defecto la clase define dos metodos que son llamados para la gestion de los
eventos y para el pintado. El primero solo mira si se recibe QUIT, saliendo de 
la aplicacion y el segundo pinta toda la ventana de blanco.

Para especificar codigo propio para la gestion de eventos basta con fijar el 
atributo event_func a la funcion que debe ser llamada. La funcion recibe un
primer parametro que es la instancia de la clase Viewer (self).

Para especificar el codigo para el pintado basta con fijar el atributo draw_func
que recibira dos parametros: la instancia a la clase Viewer (self) y el tiempo
que ha pasado desde la ultima llamada como un float (segundos).
"""

import pygame
import sys

class Viewer(object):
	Width = 0
	Height = 0

	def __init__(self):
		self.event_func = self._basic_event_handler
		self.draw_func = self._draw_func
		self.frame_rate = 60

	def set_frame_rate(rate):
		""" Fija la tasa de refresco que se intentara conseguir como maximo.
		Si no se llama a este metodo la clase usa por defecto el valor de 60.
		"""
		self.frame_rate = rate

	def init_windowed(self, res, caption):
		"""Crea una ventana con barra para titulo y boton para cerrar."""
		self.screen = pygame.display.set_mode(res)
		pygame.display.set_caption(caption)
		Viewer.Width = res[0]
		Viewer.Height = res[1]
	
	def blit(self, surface, rect):
		"""Copia la superficie 'surface' sobre la superficie de la vetana."""
		self.screen.blit(surface, rect)

	def clear(self, color):
		"""Rellena la pantalla con el color pasado como parametro."""
		self.screen.fill(color)

	def	_basic_event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)

	def _draw_func(self, time_passed):
		self.clear((255,255,255))

	def main_loop(self):
		"""Metodo que debe llamarse para inicializar la ventana y entrar
		en el bucle principal de la aplicacion"""
		self.clock = pygame.time.Clock()

		while True:
			self.event_func()
			time_passed = self.clock.tick(self.frame_rate)
			self.draw_func(time_passed)
			
			pygame.display.flip()

