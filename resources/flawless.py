import random, pyglet
from .colors import *

class Flawless(object):
	def __init__(self):
		image = self.lib.images.get("flawless.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)
		r = random.randint(0, 7)
		self.attacks = 1
		self.range = 200
		self.speed = 0.6
		self.damages = 50
		if r == 0:
			self = FlawlessAquamarine.__init__(self)
		if r == 1:
			self = FlawlessEmerald.__init__(self)
		if r == 2:
			self = FlawlessOpal.__init__(self)
		if r == 3:
			self = FlawlessSaphire.__init__(self)
		if r == 4:
			self = FlawlessDiamond.__init__(self)
		if r == 5:
			self = FlawlessTopaz.__init__(self)
		if r == 6:
			self = FlawlessAmethyst.__init__(self)
		if r == 7:
			self = FlawlessRuby.__init__(self)
		return self


class FlawlessAquamarine(object):
	def __init__(self):
		self.name = "Flawless Aquamarine"
		self.sprite.color = AQUAMARINE
		return self

class FlawlessEmerald(object):
	def __init__(self):
		#todo : poison
		self.name = "Flawless Emerald"
		self.sprite.color = EMERALD
		return self

class FlawlessOpal(object):
	def __init__(self):
		#todo : aura
		self.name = "Flawless Opal"
		self.sprite.color = OPAL
		return self

class FlawlessSaphire(object):
	def __init__(self):
		#todo: slow
		self.name = "Flawless Saphire"
		self.sprite.color = SAPHIRE
		return self

class FlawlessDiamond(object):
	def __init__(self):
		# todo: crit
		self.name = "Flawless Diamond"
		self.sprite.color = DIAMOND
		return self

class FlawlessTopaz(object):
	def __init__(self):
		self.name = "Flawless Topaz"
		self.sprite.color = TOPAZ
		return self

class FlawlessAmethyst(object):
	def __init__(self):
		# todo: ait-only
		self.name = "Flawless Amethyst"
		self.sprite.color = AMETHYST
		return self

class FlawlessRuby(object):
	def __init__(self):
		# todo : splash
		self.name = "Flawless Ruby"
		self.sprite.color = RUBY
		return self