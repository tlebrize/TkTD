import random, pyglet
from .colors import *

class Perfect(object):
	def __init__(self):
		image = self.lib.images.get("perfect.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)
		r = random.randint(0, 7)
		self.attacks = 1
		self.range = 250
		self.speed = 0.4
		self.damages = 70
		if r == 0:
			self = PerfectAquamarine.__init__(self)
		if r == 1:
			self = PerfectEmerald.__init__(self)
		if r == 2:
			self = PerfectOpal.__init__(self)
		if r == 3:
			self = PerfectSaphire.__init__(self)
		if r == 4:
			self = PerfectDiamond.__init__(self)
		if r == 5:
			self = PerfectTopaz.__init__(self)
		if r == 6:
			self = PerfectAmethyst.__init__(self)
		if r == 7:
			self = PerfectRuby.__init__(self)
		return self

class PerfectAquamarine(object):
	def __init__(self):
		self.name = "Perfect Aquamarine"
		self.sprite.color = AQUAMARINE
		return self

class PerfectEmerald(object):
	def __init__(self):
		#todo : poison
		self.name = "Perfect Emerald"
		self.sprite.color = EMERALD
		return self

class PerfectOpal(object):
	def __init__(self):
		#todo : aura
		self.name = "Perfect Opal"
		self.sprite.color = OPAL
		return self

class PerfectSaphire(object):
	def __init__(self):
		#todo: slow
		self.name = "Perfect Saphire"
		self.sprite.color = SAPHIRE
		return self

class PerfectDiamond(object):
	def __init__(self):
		# todo: crit
		self.name = "Perfect Diamond"
		self.sprite.color = DIAMOND
		return self

class PerfectTopaz(object):
	def __init__(self):
		self.name = "Perfect Topaz"
		self.sprite.color = TOPAZ
		return self

class PerfectAmethyst(object):
	def __init__(self):
		# todo: ait-only
		self.name = "Perfect Amethyst"
		self.sprite.color = AMETHYST
		return self

class PerfectRuby(object):
	def __init__(self):
		# todo : splash
		self.name = "Perfect Ruby"
		self.sprite.color = RUBY
		return self