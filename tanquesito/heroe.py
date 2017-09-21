import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.estado = "bajando"
		self.imagenes = [util.cargar_imagen('imagenes/Tanque.png'),
						util.cargar_imagen('imagenes/tanque destruido.png'),
						util.cargar_imagen('imagenes/Tanque.png'),
						util.cargar_imagen('imagenes/Tanque.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(200, 500)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_LEFT] and self.rect.x>=10:
				self.rect.x -= 10
				self.image = self.imagenes[0]
			elif teclas[K_RIGHT] and self.rect.x<=680-self.rect.width:
				self.rect.x += 10
				self.image = self.imagenes[0]
		else:
			self.image = self.imagenes[3]
