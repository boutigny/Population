from itertools import count

class city:
	ids = count(0)
	def __init__(self, name=''):
		self.name = name
		