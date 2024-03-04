import pygame
import math
import random
from pygame import Vector2
from globals import SCREEN_RECT

class Particle:
	def __init__(self, pos = Vector2(0, 0), color = (255, 255, 255), time = 10, size = 5): #these positions will be relative to the position of the particle emitter.
		self.pos = pos
		self.velo = Vector2(0, 0)
		self.color = color
		self.time = time
		self.size = size

	def update(self, screen, pos):
		self.draw(screen, pos)
		# self.gravity()
		self.randMove()
		self.time -= 1
	
	def draw(self, screen, pos):
		print("drew")
		pygame.draw.circle(screen, self.color, self.pos + pos, self.size)

	def gravity(self):
		if self.velo.y <= 1:
			self.velo.y += .05
		self.pos.y += self.velo.y

	def randMove(self):
		self.velo = Vector2(random.randint(-5, 5)/10, random.randint(-5, 5)/10)
		self.pos += self.velo


class ParticleEmitter:
	def __init__(self, pos = Vector2(0, 0), maxParticles = 10, ppf = 1): #ppf = particles per frame
		self.pos = pos
		self.maxParticles = maxParticles
		self.particleList = []
		self.ppf = ppf

	def update(self, screen, pos = None):
		print()
		if pos != None:
			self.pos = pos

		for i in range(self.ppf):
			if len(self.particleList) <= self.maxParticles:
				self.particleList.append(Particle())

		for i in range(len(self.particleList)-1, 0, -1):
			self.particleList[i].update(screen, self.pos)
			if self.particleList[i].time == 0 or not SCREEN_RECT.collidepoint(self.particleList[i].pos):
				del self.particleList[i]