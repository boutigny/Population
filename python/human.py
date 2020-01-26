class Human:
	def __init__(self, gender='female', age=0):
		if gender not in ('male', 'female'):
			raise Exception('Invalid gender - should be male or female')
		self.gender = gender
		self.age = age
		self.status = 'alive'

	def getAttributes(self):
		return self.gender, self.age, self.status