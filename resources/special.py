from .tower import Tower
from .chipped import *

class Silver(Tower):

	RECIPE = [Chipped_Saphire, Chipped_Topaz, Chipped_Diamond]

	def __init__(self, x, y, game, graphics):
		super(Silver, self).__init__(x, y, game, graphics, "silver.png")
		self.range = 79
		self.speed = 1
		self.damages = 20.5

	def splash(self, target):
		target.debuffs["slow"].append(0.5)
		def reset(_, target):
			target.debuffs["slow"].remove(0.5)
		pyglet.clock.schedule_once(reset, 3, target)

	def special(self, target):
		for mob in self.game.mobs:
			if mob is not target:
				if abs(mob.x - target.x) < 64 and abs(mob.y - target.y) < 64:
					mob.hp -= 0.5 * self.damages
					self.splash(mob)


class Malachite(Tower):

	RECIPE = [Chipped_Aquamarine, Chipped_Emerald, Chipped_Opal]

	def __init__(self, x, y, game, graphics):
		super(Malachite, self).__init__(x, y, game, graphics, "malachite.png")
		self.range = 107
		self.speed = 0.5
		self.damages = 6
		self.attacks = 3

