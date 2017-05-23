import random

class Ling(object):

	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y

	def draw(self):
		pass

	def update(self):
		self.x = (self.x + random.randint(-1, 1)) %

