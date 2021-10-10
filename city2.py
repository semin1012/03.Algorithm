class City:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
	def __str__(self):
		return str(self.__dict__)
	def s(self):
		return self.name + ':' + str(self.o) + ':' + str(self.index)
	# def __lt__

cities = [
]