import pyglet, math, random
from .chipped import Chipped
from .flawed import Flawed
from .normal import Normal
from .flawless import Flawless
from .perfect import Perfect

class Wall(object):

	def __init__(self, x, y, lib, batch):
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		image = self.lib.images.get("wall.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)

class Tower(Wall):

	def __init__(self, chance, x, y, lib, batch):
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		self.sprite = None
		roll = random.randint(0, chance)
		if roll > 100:
			self = Perfect.__init__(self)
		elif roll > 80:
			self = Flawless.__init__(self)
		elif roll > 50:
			self = Normal.__init__(self)
		elif roll > 20:
			self = Flawed.__init__(self)
		else:
			self = Chipped.__init__(self)
		print(self.name)

	def clear(self, dt, sprite):
		sprite.delete()

	def hit(self, target):
		target.hp -= self.damages
		hit_image = self.lib.images.get("hit.png")
		hit_sprite = pyglet.sprite.Sprite(hit_image,
					x=target.sprite.x, y=target.sprite.y, batch=self.batch)
		hit_sprite.color = self.sprite.color
		pyglet.clock.schedule_once(self.clear, 0.2, hit_sprite)

	def set_sprite(self, name):
		if self.sprite:
			self.sprite.delete()
		image = self.lib.images.get(name)
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)

	def play(self, dt=None, mobs=None):
		if not self.running or mobs == None:
			return
		attacks = self.attacks
		sx = self.x * 32 + 16
		sy = self.y * 32 + 16
		for mob in mobs:
			mx = mob.sprite.x + 16
			my = mob.sprite.y + 16
			if math.sqrt(((sx - mx) ** 2) + ((sy - my) ** 2)) < self.range:
				self.hit(mob)
				attacks -= 1
				if attacks <= 0:
					break
		pyglet.clock.schedule_once(self.play, self.speed, mobs)

