class Cell(object):

	def __init__(self, x, y, graphics):
		self.x = x
		self.y = y
		self.graphics = graphics
		self.content = None
		self.sprite = None
		self.walkable = True
		self.neighbors = None
		self.next = [None, None, None]
		self.effects = {}

	def add_effect(self, name, z=2):
		if not self.effects.get(name):
			sprite = self.graphics.load_sprite(name,
				x=self.x*32, y=self.y*32, z=z)
			self.effects.update({name: sprite})

	def delete_effect(self, name=False):
		if not name:
			for sprite in self.effects:
				self.effects.get(sprite).delete()
			self.effects = {}
		elif self.effects.get(name):
			self.effects.get(name).delete()
			self.effects.pop(name)
