from itertools import count

class Human:
	_ids = count(0)
	def __init__(self, gender='female', age=0, city=''):
		if gender not in ('male', 'female'):
			raise Exception('Invalid gender - should be male or female')
		self._gender = gender
		self._age = age
		self._status = 'alive'
		self._city = city
		self._id = next(self._ids)

	def getAttributes(self):
		return self._id, self._gender, self._age, self._status, self._city

	def kill(self):
		self._status = 'dead'

	def moveTo(self, city):
		self._city = city
