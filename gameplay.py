

# from app import scoresWindow

import pygame, sys

from layout import Button, Menu
from objects import *
from window import BaseWindow, Window
from handleScore import getScore

pygame.init()
pygame.mixer.init()



def allowedEvent():
    pygame.event.set_blocked(pygame.ACTIVEEVENT)
    # pygame.event.set_blocked(pygame.KEYDOWN)
    pygame.event.set_blocked(pygame.KEYUP)
    # pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
    # pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.JOYAXISMOTION)
    pygame.event.set_blocked(pygame.JOYBALLMOTION)
    pygame.event.set_blocked(pygame.JOYHATMOTION)
    pygame.event.set_blocked(pygame.JOYBUTTONUP)
    pygame.event.set_blocked(pygame.JOYBUTTONDOWN)
    pygame.event.set_blocked(pygame.VIDEORESIZE)
    pygame.event.set_blocked(pygame.VIDEOEXPOSE)
    pygame.event.set_blocked(pygame.USEREVENT)

    # pygame.event.set_blocked(3)




def printText(surf,pos,text):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render(str(text), True, (10,10,10))
    surf.blit(text,pos)




def changetoMainMenu():
	Window.setWindowName("MainMenu")

class GamePlay(BaseWindow):
	def __init__(self):
		super().__init__()
		self.size = (w,h) = (400,600)
		self.bg = pygame.Surface((w,h))
		self.bg.fill((100,50,190))
		self.clock = pygame.time.Clock()
		self.highScore = getScore()[0]["score"]
		self.fps = 15 

		self._objects = snake,food = [Snake(),Food()]

		self.pauseButton = Button((w//2+160-80,500),(80,40), "Pause",snake.stop)
		self.mainMenuButton = Button((w//2-160,500),(80,40), "Menu",changetoMainMenu)
		self.pause_menu = Menu((w//2-40,h//2-(20)*2),(80,40),["Resume","Menu"],[snake.resume,changetoMainMenu])
		self.music = pygame.mixer.Sound('sounds/TS - Beat Y.ogg')
		self.music.play(loops=-1, maxtime=0, fade_ms=1000)


		allowedEvent()
	def __del__(self):
		self.music.stop()

	def quit(self):
		pygame.quit()
		sys.exit()

	def checkEvents(self,ev):
		if ev.type == pygame.QUIT:
			quit()
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_ESCAPE:
				# running = False
				quit()

		for o in self._objects:
			o.checkEvents(ev)

		self.pauseButton.checkEvents()
		self.mainMenuButton.checkEvents()

		snake = self._objects[0]
		if snake.isstop:
			self.pause_menu.checkEvents()

			pygame.mixer.pause()
		else :
			pygame.mixer.unpause()

		

	def update(self):
		snake,food = self._objects
		snake.move()
		snake.eat(food)

	def draw(self,surf):
		w,h = self.size
		snake = self._objects[0]
		surf.blit(self.bg,(0,0))

		for o in self._objects:
			o.draw(surf)

		pygame.draw.rect(surf,(80,30,150),pygame.Rect((0,498), (400,600-498)))
		pygame.draw.line(surf,(50,50,50),(0,498),(400,498),1)

		self.pauseButton.draw(surf)
		self.mainMenuButton.draw(surf)

		if snake.isstop:
			color = pygame.Color(80, 30, 150, a=10)
			color.a=0
			# pygame.draw.rect(surf,color,pygame.Rect((w//2-140,h//2-(50)*2), (400,600-498)))
			self.pause_menu.draw(surf)

		printText(surf,(0,0),"SCORE: {}".format(snake.score))
		printText(surf,(250,0),"HIGHSCORE: {}".format(self.highScore))

