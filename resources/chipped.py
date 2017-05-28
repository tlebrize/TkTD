import pyglet, random
from .color import *
from .tower import Tower

class Chipped(Tower):
	def __init__(self, x, y, game, graphics, color):
		super(Chipped, self).__init__(x, y, game, graphics, "chipped.png", color)
		self.range = 72
		self.speed = 0.8
		self.damages = 11

class Chipped_Aquamarine(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Aquamarine, self).__init__(x, y, game, graphics, Aquamarine)
		self.speed = 0.5
		self.range = 50
		self.damages = 7
		self.effect = "Faster attacks"

class Chipped_Emerald(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Emerald, self).__init__(x, y, game, graphics, Emerald)
		self.range = 79
		self.speed = 1
		self.effect = "Poison and slowing attacks"

	def special(self, target):
		target.debuffs["slow"].append(0.85)
		target.debuffs["poison"].append(2)
		def reset(_, target):
			target.debuffs["slow"].remove(0.85)
			target.debuffs["poison"].remove(2)
		pyglet.clock.schedule_once(reset, 3, target)

class Chipped_Opal(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Opal, self).__init__(x, y, game, graphics, Opal)
		self.range = 86
		self.damages = 4.5
		self.effect = "Speed Aura"

class Chipped_Saphire(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Saphire, self).__init__(x, y, game, graphics, Saphire)
		self.range = 72
		self.damages = 6.5
		self.effect = "Slowing attacks"

	def special(self, target):
		target.debuffs["slow"].append(0.5)
		def reset(_, target):
			target.debuffs["slow"].remove(0.5)
		pyglet.clock.schedule_once(reset, 3, target)

class Chipped_Diamond(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Diamond, self).__init__(x, y, game, graphics, Diamond)
		self.damages = 10
		self.effect = "Ground only and critical hits chance"
		self.targets = ["ground"]

	def special(self, target):
		if random.randint(0, 100) > 25:
			target.hp -= self.damages

class Chipped_Topaz(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Topaz, self).__init__(x, y, game, graphics, Topaz)
		self.damages = 4
		self.attacks = 3
		self.effect = "Hits multiple targets"

class Chipped_Amethyst(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Amethyst, self).__init__(x, y, game, graphics, Amethyst)
		self.range = 143
		self.effect = "Attacks air only"
		self.targets = ["air"]

class Chipped_Ruby(Chipped):
	def __init__(self, x, y, game, graphics):
		super(Chipped_Ruby, self).__init__(x, y, game, graphics, Ruby)
		self.range = 114
		self.damages = 8.5
		self.speed = 1
		self.effect = "Splash damages"

	def special(self, target):
		for mob in self.game.mobs:
			if mob is not target:
				if abs(mob.x - target.x) < 64 and abs(mob.y - target.y) < 64:
					mob.hp -= 0.5 * self.damages




