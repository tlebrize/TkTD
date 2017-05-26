import random, pyglet
from .colors import *

class Flawed(object):
	def __init__(self):
		image = self.lib.images.get("flawed.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)
		r = random.randint(0, 7)
		self.attacks = 1
		self.range = 125
		self.speed = 0.9
		self.damages = 17
		if r == 0:
			self = FlawedAquamarine.__init__(self)
		if r == 1:
			self = FlawedEmerald.__init__(self)
		if r == 2:
			self = FlawedOpal.__init__(self)
		if r == 3:
			self = FlawedSaphire.__init__(self)
		if r == 4:
			self = FlawedDiamond.__init__(self)
		if r == 5:
			self = FlawedTopaz.__init__(self)
		if r == 6:
			self = FlawedAmethyst.__init__(self)
		if r == 7:
			self = FlawedRuby.__init__(self)
		return self


class FlawedAquamarine(object):
	def __init__(self):
		self.name = "Flawed Aquamarine"
		self.sprite.color = AQUAMARINE
		return self

class FlawedEmerald(object):
	def __init__(self):
		#todo : poison
		self.name = "Flawed Emerald"
		self.sprite.color = EMERALD
		return self

class FlawedOpal(object):
	def __init__(self):
		#todo : aura
		self.name = "Flawed Opal"
		self.sprite.color = OPAL
		return self

class FlawedSaphire(object):
	def __init__(self):
		#todo: slow
		self.name = "Flawed Saphire"
		self.sprite.color = SAPHIRE
		return self

class FlawedDiamond(object):
	def __init__(self):
		# todo: crit
		self.name = "Flawed Diamond"
		self.sprite.color = DIAMOND
		return self

class FlawedTopaz(object):
	def __init__(self):
		self.name = "Flawed Topaz"
		self.sprite.color = TOPAZ
		return self

class FlawedAmethyst(object):
	def __init__(self):
		# todo: ait-only
		self.name = "Flawed Amethyst"
		self.sprite.color = AMETHYST
		return self

class FlawedRuby(object):
	def __init__(self):
		# todo : splash
		self.name = "Flawed Ruby"
		self.sprite.color = RUBY
		return self

