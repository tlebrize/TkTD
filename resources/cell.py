import pyglet
from .objects import Tower

class Cell(object):

	def __init__(self, x, y, lib, batch):
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		self.neighbors = {}
		self.color = (0.2, 0.2, 0.2)
		self.effects = {}
		self.content = None
		self.next = None

	def add_effect(self, name):
		if not self.effects.get(name):
			image = self.lib.images.get(name)
			sprite = pyglet.sprite.Sprite(image, batch=self.batch)
			sprite.x = self.x * 32
			sprite.y = self.y * 32
			self.effects.update({name: sprite})

	def delete_effect(self, name=False):
		if not name:
			for sprite in self.effects:
				self.effects.get(sprite).delete()
			self.effects = {}
		elif self.effects.get(name):
			self.effects.get(name).delete()
			self.effects.pop(name)

	def select(self):
		self.add_effect("selected.png")

	def deselect(self):
		self.delete_effect("selected.png")

	def add_tower(self, name):
		if self.content == None:
			self.content = Tower(name, self.x, self.y, self.lib, self.batch)

	def delete_tower(self):
		if isinstance(self.content, Tower):
			self.content.sprite.delete()
			self.content = None

