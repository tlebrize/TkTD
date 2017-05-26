import random, pyglet
from .colors import *

class Chipped(object):
	def __init__(self):
		image = self.lib.images.get("chipped.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)
		self.attacks = 1
		self.range = 100
		self.speed = 1
		self.damages = 10
		r = random.randint(0, 7)
		if r == 0:
			self = ChippedAquamarine.__init__(self)
		if r == 1:
			self = ChippedEmerald.__init__(self)
		if r == 2:
			self = ChippedOpal.__init__(self)
		if r == 3:
			self = ChippedSaphire.__init__(self)
		if r == 4:
			self = ChippedDiamond.__init__(self)
		if r == 5:
			self = ChippedTopaz.__init__(self)
		if r == 6:
			self = ChippedAmethyst.__init__(self)
		if r == 7:
			self = ChippedRuby.__init__(self)
		return self

class ChippedAquamarine(object):
	def __init__(self):
		self.name = "Chipped Aquamarine"
		self.speed = 0.7
		self.sprite.color = AQUAMARINE
		return self

class ChippedEmerald(object):
	def __init__(self):
		#todo : poison
		self.name = "Chipped Emerald"
		self.range = 300
		self.sprite.color = EMERALD
		return self

class ChippedOpal(object):
	def __init__(self):
		#todo : aura
		self.name = "Chipped Opal"
		self.sprite.color = OPAL
		return self

class ChippedSaphire(object):
	def __init__(self):
		#todo: slow
		self.name = "Chipped Saphire"
		self.sprite.color = SAPHIRE
		return self

class ChippedDiamond(object):
	def __init__(self):
		# todo: crit
		self.name = "Chipped Diamond"
		self.sprite.color = DIAMOND
		return self

class ChippedTopaz(object):
	def __init__(self):
		self.name = "Chipped Topaz"
		self.attacks = 3
		self.damages = 5
		self.sprite.color = TOPAZ
		return self

class ChippedAmethyst(object):
	def __init__(self):
		# todo: ait-only
		self.name = "Chipped Amethyst"
		self.sprite.color = AMETHYST
		return self

class ChippedRuby(object):
	def __init__(self):
		# todo : splash
		self.name = "Chipped Ruby"
		self.sprite.color = RUBY
		return self