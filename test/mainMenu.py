
import pygame, sys
import gameplay
import leaderbord

from layout import Menu
from window import Window
from window import baseWindow
from gameplay import GamePlay

pygame.init()


def quit():
	pygame.quit()
	sys.exit()

def changetoplay():
	Window.setWindow(GamePlay())

class MainMenu(baseWindow):
	def __init__(self):
		super().__init__()
		self.size = (w,h) = (400,600)
		self.bg = pygame.Surface((w,h))
		self.bg.fill((100,50,190))
		self.menu = Menu((w//2-40,h//2-(20)*4),(80,40),["Play","Scores","Settings","Quit"],[changetoplay,leaderbord.main,None,quit])
		self.clock = pygame.time.Clock()

	def checkEvents(self,ev):
		if ev.type == pygame.QUIT:
			quit()
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_ESCAPE:
				# running = False
				quit()

		self.menu.checkEvents()

	def draw(self,surf):
		surf.blit(self.bg,(0,0))
		self.menu.draw(surf)






def main():
	w,h = 400,600
	screen = pygame.display.set_mode((w,h))

	Window.setWindow(MainMenu())



	running=True
	while running:
		Window.current.clock.tick(20)

		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				running = False
			if ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_ESCAPE:
					# running = False
					quit()

			Window.current.checkEvents(ev)

		Window.current.update()
		Window.current.draw(screen)

		pygame.display.update()

if __name__ =="__main__":
	main()