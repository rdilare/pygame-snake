import json
import pygame, sys
import datetime as dt

pygame.init()

class LeaderBoard:
	data=[]
	def __init__(self):

		self.loadData()

	@classmethod
	def loadData(cls):

		with open("scores.txt","r") as f:
			f.seek(0)
			cls.data = json.loads(f.read())
			f.close()

	@classmethod
	def getdata(cls):
		cls.loadData()
		return cls.data

	def draw(self,surf):
		font = pygame.font.SysFont("comicsansms", 25)

		sr_title = font.render("Sr.", True, (0,0,0))
		date_title = font.render("DATE", True, (0,0,0))
		score_title = font.render("SCORE", True, (0,0,0))

		surf.blit(sr_title,(50,200))
		surf.blit(date_title,(90,200))
		surf.blit(score_title,(260,200))

		j=1
		for i in self.data:
			sr = font.render(str(j)+".", True, (255,255,0))
			date = font.render(str(i["date"]), True, (255,255,0))
			score = font.render(str(i["score"]), True, (255,255,0))

			surf.blit(sr,(50,200+j*20))
			surf.blit(date,(90,200+j*20))
			surf.blit(score,(260,200+j*20))
			j+=1

	def saveScore(self,score):
		date = dt.datetime.now()
		with open("scores.txt","r") as f:

			f.seek(0)
			x = json.loads(f.read())
			f.close()

			x.append({"date":date.strftime("%d-%b %Y"), "score":score})
			x.sort(key = lambda i:i["score"], reverse=True)

			if len(x)>5:x=x[:5]
			
			y = json.dumps(x)

			f = open("scores.txt","w")
			f.write(y)
			f.close()

			self.loadData()


def main():
	screen = pygame.display.set_mode((400,600))
	clock = pygame.time.Clock()

	l = LeaderBoard()

	running = True
	while running:
		clock.tick(1)

		for ev in pygame.event.get():
			if ev.type==pygame.QUIT:
				sys.exit()
			if ev.type==pygame.KEYDOWN:
				if ev.key==pygame.K_ESCAPE:
					sys.exit()


		screen.fill((100,50,190))

		l.draw(screen)

		pygame.display.update()

if __name__=="__main__":
	main()