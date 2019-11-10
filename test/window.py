

class baseWindow:
	def checkEvents(self):
		pass

	def draw(self):
		pass

	def update(self):
		pass

class Window:
	current = None

	@classmethod
	def setWindow(cls,a):
		cls.current = a

