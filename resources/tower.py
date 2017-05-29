import random, pyglet, math

class Rock(object):
	def __init__(self, x, y, graphics):
		self.sprite = graphics.load_sprite("rock.png",
			x=x,  y=y, z=1)

	def __str__(self):
		return "Rock"


class Tower(object):
	def __init__(self, x, y, game, graphics, sprite, color=None):
		self.x = x
		self.y = y
		self.game = game
		self.graphics = graphics
		self.color = color
		self.sprite = self.graphics.load_sprite(sprite,
			x=x, y=y, z=1, color=color)
		self.attacks = 1
		self.targets = ["ground", "air"]
		self.combines_into = None

	def __str__(self):
		return str(type(self).__name__).replace("_", " ")

	def hit(self, target):
		if target.terrain not in self.targets:
			return
		self.special(target)
		target.hp -= self.damages
		projectile = self.graphics.load_sprite("hit.png",
			x=target.sprite.x, y=target.sprite.y, z=2, color=self.color)
		pyglet.clock.schedule_once(lambda _, p: p.delete(), 0.2, projectile)

	def special(self, target):
		pass

	def play(self, _=None):
		if self.game.running:
			attacks = self.attacks
			sx = self.sprite.x
			sy = self.sprite.y
			for mob in self.game.mobs:
				mx = mob.sprite.x + 16
				my = mob.sprite.y + 16
				if math.sqrt(((sx - mx) ** 2) + ((sy - my) ** 2)) < self.range:
					if attacks > 0:
						attacks -= 1
						self.hit(mob)
					else:
						break
		pyglet.clock.schedule_once(self.play, self.speed)