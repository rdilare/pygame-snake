import pygame, sys
import gameplay

from math import *

pygame.font.init()
pygame.init()

yellow = (255,200,0)

global screen

screen_w = 400
screen_h = 600

screen = pygame.display.set_mode((screen_w,screen_h))
screen.fill((0,50,190))

ts = pygame.Surface(screen.get_size())
ts.fill((0,200,50))

screen.blit(ts,[0,0])

color = pygame.Color(220,50,0,a=1)

clock = pygame.time.Clock()




# class Circle:
# 	def __init__(self,x,y,r):
# 		self.pos = [x,y]
# 		self.radius = r
# 		self.vel = [0,0]
	
# 	def draw(self,surf):
# 		pygame.draw.circle(surf,(200,0,0),self.pos,self.radius)
	
# 	def addVel(self,x,y):
# 		self.vel = [x,y]

# 		self.pos[0]+=x
# 		self.pos[1]+=y

# 		w,h = pygame.display.get_surface().get_size()

# 		if self.pos[0]>w: self.pos[0]=0
# 		if self.pos[0]<0: self.pos[0]=w
# 		if self.pos[1]>h: self.pos[1]=0
# 		if self.pos[1]<0: self.pos[1]=h



def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
 
# obj = Circle(200,300,5)

global i
i = 0

def gameWindow():
	global i
	
	gameplay.main()

	# src = pygame.display.get_surface()
	# w,h = src.get_size()
	# gw = pygame.Surface((w,h))
	# gw.fill(yellow)

	# i+=.1

	# obj.addVel(int(30*cos(i)),-int(30*sin(i)))
	# # obj.addVel(5,2)
	# obj.draw(gw)

	# button(gw,"Main Menu", 20,500,100,30, pygame.Color(0,50,200,a=1),(240,70,0), mainWindow)
	# button(gw,"Quit", 280,500,100,30, (0,50,200),(240,70,0), quitgame)

	# src.blit(gw,[0,0])

	# # print(">>gameWindow(){}".format(gw.get_size()))

def scoresWindow():
	src = pygame.display.get_surface()
	sw = pygame.Surface(src.get_size())
	sw.fill(yellow)

	drawMenu(["Score1","Score2","Score3","Score4","Score5"],sw,mid = True)

	button(sw,"Main Menu", 20,500,100,30, (0,50,200),(240,70,0), mainWindow)
	button(sw,"Quit", 280,500,100,30, (0,50,200),(240,70,0), quitgame)

	src.blit(sw,[0,0])

	# print(">>gameWindow(){}".format(gw.get_size()))

def button(bg,msg,x,y,w,h,ic,ac,action=None):
	global current_window
	screen = pygame.display.get_surface()
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	menuScreen  = bg
	

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(menuScreen, ac,(x,y,w,h))
		if click[0] == 1 and action != None:
			current_window = action         
	else:
		pygame.draw.rect(menuScreen, ic,(x,y,w,h))

	smallText = pygame.font.SysFont("comicsansms",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	menuScreen.blit(textSurf, textRect)

	screen.blit(menuScreen,(0,0))


def drawMenu(items,bg,action=None,mid = False):

	global screen
	screen_w,screen_h = screen.get_size()
	
	menuScreen = bg

	if not action:
		action  = [None for i in range(len(items))]

	[posx,posy,item_w,item_h] = [100,200,100,30]

	if mid:
		posx = (screen_w/2) - item_w/2

	for i in range(len(items)):
		# pygame.draw.rect(screen, color, [posx,posy+(1.05*i*item_h),item_w,item_h])
		button(menuScreen,items[i], posx,posy+(i*(item_h+1)),item_w,item_h, (0,50,200),(240,70,0), action[i])

def mainWindow():
	global screen
	screen.fill(yellow)
	bg = screen
	drawMenu(["Play","High Scores","Settings","Quit"],bg,[gameWindow,scoresWindow,None,quitgame],mid = True)
	

global done
done = False


def gameloop():
	global done, current_window
	current_window = mainWindow
	while not done:

		for ev in pygame.event.get():
			if ev.type==pygame.QUIT:
				done = True

		current_window()
		
		# drawMenu(["1item"])
		pygame.display.flip()
		# pygame.display.update([150,200,100,200])
		clock.tick(30)


def quitgame():
	# pygame.display.quit()
	pygame.quit()
	# sys.exit()


try:
	mainWindow()
	gameloop()

finally:
	# pygame.display.quit()
	pygame.quit()
	# sys.exit(0)