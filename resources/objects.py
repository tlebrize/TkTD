import pyglet, math

class Object(object):
	pass

class Tower(Object):

	def __init__(self, name, x, y, lib, batch):
		self.x = x
		self.y = y
		self.name = name
		self.lib = lib
		self.batch = batch
		self.sprite = None
		self.set_sprite(self.name)

	def set_sprite(self, name):
		if self.sprite:
			self.sprite.delete()
		self.name = name
		image = self.lib.images.get(self.name)
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)

	def play(self, dt=None, mobs=None):
		if not self.running or mobs == None:
			return
		sx = self.x * 32 + 16
		sy = self.y * 32 + 16
		for mob in mobs:
			mx = mob.sprite.x + 16
			my = mob.sprite.y + 16
			if math.sqrt(((sx - mx) ** 2) + ((sy - my) ** 2)) < 100:
				mob.hit()
				break
		pyglet.clock.schedule_once(self.play, 1, mobs)

class Wall(Object):

	def __init__(self, x, y, lib, batch):
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		image = self.lib.images.get("wall.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)

class Checkpoint(object):

	def __init__(self, next, x, y, lib, batch):
		self.next = next
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		image = self.lib.images.get("check.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)
