

# from app import scoresWindow

import pygame, sys

from layout import Button, Menu
from leaderbord import LeaderBoard
from objects import *
from window import baseWindow

pygame.init()



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
    text = font.render(str(text), True, (255,150,0))
    surf.blit(text,pos)

def pauseMenu(surf):
	w,h = pygame.display.get_surface().get_size()
	resume = Button((w//2-50,200),(80,40), "resume")
	mainMenu = Button((100,250),(80,40), "menu")

	pygame.draw.rect(surf,(255,0,0),((w//2)-120,(h//2)-150,240,300))

	resume.checkEvents()
	mainMenu.checkEvents()

	resume.draw(surf)
	mainMenu.draw(surf)


class GamePlay(baseWindow):
	def __init__(self):
		super().__init__()
		self.size = (w,h) = (400,600)
		self.bg = pygame.Surface((w,h))
		self.bg.fill((100,50,190))
		self.clock = pygame.time.Clock()

		self._objects = snake,food = [Snake(),Food()]

		self.button = Button((100,500),(80,40), "pause",snake.stop)
		self.pause_menu = Menu((w//2-40,h//2-(20)*2),(80,40),["resume","menu"],[snake.resume,None])

		allowedEvent()

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

		self.button.checkEvents()

		if self._objects[0].isstop:
			self.pause_menu.checkEvents()

	def update(self):
		snake,food = self._objects
		snake.move()
		snake.eat(food)

	def draw(self,surf):
		snake = self._objects[0]
		surf.blit(self.bg,(0,0))

		for o in self._objects:
			o.draw(surf)

		self.button.draw(surf)
		if snake.isstop:
			self.pause_menu.draw(surf)

		printText(surf,(0,0),"score: {}".format(snake.score))
		printText(surf,(250,0),"Highscre: {}".format(LeaderBoard.getdata()[0]["score"]))



def main():

	screen = pygame.display.set_mode((400,600))

	w,h = screen.get_size()

	snake = Snake()
	food = Food()


	button = Button((100,500),(80,40), "pause",snake.stop)
	pause_menu = Menu((w//2-40,h//2-(20)*2),(80,40),["resume","menu"],[snake.resume,None])
	
	clock = pygame.time.Clock()

	allowedEvent()



	ev = pygame.event.peek()

	running = True
	while running:
		clock.tick(10)



		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				running = False
			if ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_ESCAPE:
					# running = False
					quit()

			snake.checkEvents(ev)
			food.checkEvents(ev)
			button.checkEvents()


		screen.fill((100,50,190))
		
		pygame.event.clear()

		snake.move()
		snake.eat(food)

		food.draw(screen)
		button.draw(screen)
		snake.draw(screen)

		if snake.isstop:
			pause_menu.checkEvents()
			pause_menu.draw(screen)
			pass

		printText(screen,(0,0),"score: {}".format(snake.score))
		printText(screen,(250,0),"Highscre: {}".format(LeaderBoard.getdata()[0]["score"]))



		pygame.display.update()





# main()

if __name__=="__main__":
	main()
