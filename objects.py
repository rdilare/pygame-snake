import pygame
import random

from math import *


# from layout import Button, Menu
from handleScore import saveScore

pygame.init()


class grid:
	w,h =(400,500)
	cellsize = 8
	gridsize = (w//cellsize, h//cellsize)

	def getRandomPos():
		c,r = (random.randint(0,grid.gridsize[0]-1), random.randint(0,grid.gridsize[1]-1))
		return (c*grid.cellsize, r*grid.cellsize)



class Block:
	def __init__(self):
		self.pos = (0,0)
		self.color = (255,255,0)
		self.step = grid.cellsize
		self.size = (grid.cellsize-1,grid.cellsize-1)
		self.rect = pygame.Rect(self.pos, self.size)

	def draw(self,surf):
		pygame.draw.rect(surf,self.color,pygame.Rect(self.pos, self.size))


	def getpos(self):
		return self.pos

	def setpos(self,pos):
		self.pos = pos
		self.rect = pygame.Rect(self.pos, self.size)


class Food:
	def __init__(self):
		w,h = pygame.display.get_surface().get_size()
		self.pos = grid.getRandomPos()
		self.size = (grid.cellsize-1,grid.cellsize-1)
		self.color = (0,255,0)

	def draw(self,surf):
		pygame.draw.rect(surf,self.color,pygame.Rect(self.pos, self.size))

	def update(self):
		ncol, nrow = grid.gridsize
		r,c = (random.randint(0,nrow-1), random.randint(0,ncol-1))
		self.pos = (grid.cellsize*c, grid.cellsize*r)

	def checkEvents(self,ev):
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_c:
					self.update()



class Snake():
	def __init__(self):
		self.head = Block()
		self.body = [Block() for i in range(5)]
		self.isstop = False
		self.isdead = False
		self.head.color = (0,0,0)
		self.step = grid.cellsize
		self.direction = [1,0]

		self.score = 0

		self.turned = False

		for i in range(len(self.body)):
			l = len(self.body)
			a = grid.cellsize
			pos = (0,(l-i)*a)
			self.body[i].setpos(pos)

		self.head.setpos((0,len(self.body)*self.step))

	def __del__(self):
		saveScore(self.score)

	def add(self,b):  # b is Block instance
		self.body.append(b)

	def move(self,direction=None):



		# w,h = pygame.display.get_surface().get_size()
		w,h = grid.gridsize
		w,h = (w*grid.cellsize,h*grid.cellsize)

		hp = self.head.getpos()
		if not direction:
			# if self.turned:
			# 	self.turned=False
			# 	return
			direction = self.direction

		
		newheadpos = (hp[0]+direction[0]*self.step, hp[1]+direction[1]*self.step)
		
		if newheadpos == self.body[0].pos:

			direction = ((self.head.pos[0]-self.body[0].pos[0])//self.step,(self.head.pos[1]-self.body[0].pos[1])//self.step)
			newheadpos = (hp[0]+direction[0]*self.step, hp[1]+direction[1]*self.step)

	#------------Collision detection with body-----------------
		for i in self.body:
			if newheadpos == i.pos:
				self.isdead=True
				self.stop()
				break

	#------------Collision detection with Boundaries-----------------
		if newheadpos[0]<0:
			self.isdead = True
			self.stop()
		if newheadpos[0] + self.head.size[0]>w:
			self.isdead = True
			self.stop()
		if newheadpos[1]<0:
			self.isdead = True
			self.stop()
		if newheadpos[1] + self.head.size[1]>h:
			self.isdead = True
			self.stop()


		if not self.isstop:
			npos = self.head.getpos()
			self.head.setpos(newheadpos)

			for i in self.body:
				pos=i.getpos()
				i.setpos(npos)
				npos = pos
		return

	def draw(self,surf):
		self.head.draw(surf)

		for i in self.body:
			i.draw(surf)

	def stop(self):
		self.isstop = True
		pygame.mixer.pause()
	def resume(self):
		self.isstop = False
	def restart(self):
		self.__init__()

	def eat(self,f):

		if f.pos==self.head.pos:
			self.score+=1
			n = Block()
			n.pos = f.pos
			self.add(n)
			f.update()

	def checkEvents(self,ev):
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_UP:
				self.direction = (0,-1)
				# self.isstop = False
			elif ev.key == pygame.K_DOWN:
				self.direction = (0,1)
				# self.isstop = False
			elif ev.key == pygame.K_RIGHT:
				self.direction = (1,0)
				# self.isstop = False
			elif ev.key == pygame.K_LEFT:
				self.direction = (-1,0)
				# self.isstop = False
			
			# self.move()
			self.turned =True
