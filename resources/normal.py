import random, pyglet
from .colors import *

class Normal(object):
	def __init__(self):
		image = self.lib.images.get("normal.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)
		r = random.randint(0, 7)
		self.attacks = 1
		self.range = 175
		self.speed = 0.8
		self.damages = 25
		if r == 0:
			self = NormalAquamarine.__init__(self)
		if r == 1:
			self = NormalEmerald.__init__(self)
		if r == 2:
			self = NormalOpal.__init__(self)
		if r == 3:
			self = NormalSaphire.__init__(self)
		if r == 4:
			self = NormalDiamond.__init__(self)
		if r == 5:
			self = NormalTopaz.__init__(self)
		if r == 6:
			self = NormalAmethyst.__init__(self)
		if r == 7:
			self = NormalRuby.__init__(self)
		return self

class NormalAquamarine(object):
	def __init__(self):
		self.name = "Normal Aquamarine"
		self.sprite.color = AQUAMARINE
		return self

class NormalEmerald(object):
	def __init__(self):
		#todo : poison
		self.name = "Normal Emerald"
		self.sprite.color = EMERALD
		return self

class NormalOpal(object):
	def __init__(self):
		#todo : aura
		self.name = "Normal Opal"
		self.sprite.color = OPAL
		return self

class NormalSaphire(object):
	def __init__(self):
		#todo: slow
		self.name = "Normal Saphire"
		self.sprite.color = SAPHIRE
		return self

class NormalDiamond(object):
	def __init__(self):
		# todo: crit
		self.name = "Normal Diamond"
		self.sprite.color = DIAMOND
		return self

class NormalTopaz(object):
	def __init__(self):
		self.name = "Normal Topaz"
		self.sprite.color = TOPAZ
		return self

class NormalAmethyst(object):
	def __init__(self):
		# todo: ait-only
		self.name = "Normal Amethyst"
		self.sprite.color = AMETHYST
		return self

class NormalRuby(object):
	def __init__(self):
		# todo : splash
		self.name = "Normal Ruby"
		self.sprite.color = RUBY
		return self
