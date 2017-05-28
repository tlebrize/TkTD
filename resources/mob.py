import pyglet

class Mob(object):

	COLORS = [	(255, 255, 255), (255, 120, 255), (120, 255, 255), (255, 255, 120),
				(120, 255, 120), (120, 120, 255), (255, 120, 120), (90, 90, 90)]

	def __init__(self, game, level, kind, color):
		self.game = game
		self.x = self.game.checkpoints[0].x * 32
		self.y = self.game.checkpoints[0].y * 32
		self.sprite = self.game.graphics.load_sprite(kind,
			x=self.x, y=self.y, z=1, color=Mob.COLORS[color])
		self.checkpoint = 0
		self.current = self.game.checkpoints[0]
		self.speed = 4
		self.base_speed = 4
		self.debuffs =  {"poison": [], "slow": [1]}
		self.terrain = "ground"
		pyglet.clock.schedule_interval(self._move, 1/30)
		pyglet.clock.schedule_interval(self._poison, 1)

	def __str__(self):
		return str(type(self).__name__)

	def _poison(self, _):
		for poison in self.debuffs["poison"]:
			self.hp -= poison

	def _get_speed(self):
		self.speed = self.base_speed * min(self.debuffs["slow"])

	def _move(self, _):
		self._get_speed()
		if self.hp < 0:
			self.sprite.delete()
			self.game.mobs.remove(self)
			pyglet.clock.unschedule(self._move)
			return
		while self.checkpoint < len(self.game.checkpoints) - 1 and not self.current.next[self.checkpoint]:
			self.checkpoint += 1
		if self.checkpoint == len(self.game.checkpoints) - 1:
			self.game.hp -= 1
			self.sprite.delete()
			self.game.mobs.remove(self)
			pyglet.clock.unschedule(self._move)
		elif not self.current.next[self.checkpoint]:
			raise Exception("Invalid path.")
		else:
			checkpoint = self.current.next[self.checkpoint]
			if self.sprite.x < checkpoint.x*32:
				self.sprite.x += min([self.speed, checkpoint.x*32 - self.sprite.x])
			elif self.sprite.x > checkpoint.x*32:
				self.sprite.x -= min([self.speed, self.sprite.x - checkpoint.x*32])
			if self.sprite.y < checkpoint.y*32:
				self.sprite.y += min([self.speed, checkpoint.y*32 - self.sprite.y])
			elif self.sprite.y > checkpoint.y*32:
				self.sprite.y -= min([self.speed, self.sprite.y - checkpoint.y*32])
			if all([self.sprite.x == self.current.next[self.checkpoint].x*32,
						self.sprite.y == self.current.next[self.checkpoint].y*32]):
				self.current = self.current.next[self.checkpoint]
			self.x = self.sprite.x
			self.y = self.sprite.y


class Angel(Mob):
	def __init__(self, game, level, color):
		super(Angel, self).__init__(game, level, "angel.png", color)
		self.hp = 10 + 10 * level
		self.terrain = "air"

	def _move(self, _):
		self._get_speed()
		if self.hp < 0:
			self.sprite.delete()
			self.game.mobs.remove(self)
			pyglet.clock.unschedule(self._move)
			return
		if all([self.sprite.x == self.game.checkpoints[self.checkpoint+1].x*32,
					self.sprite.y == self.game.checkpoints[self.checkpoint+1].y*32]):
			self.checkpoint += 1
		if self.checkpoint == len(self.game.checkpoints) - 1:
			self.game.hp -= 1
			self.sprite.delete()
			pyglet.clock.unschedule(self._move)
		else:
			checkpoint = self.game.checkpoints[self.checkpoint+1]
			if self.sprite.x < checkpoint.x*32:
				self.sprite.x += min([self.speed, checkpoint.x*32 - self.sprite.x])
			elif self.sprite.x > checkpoint.x*32:
				self.sprite.x -= min([self.speed, self.sprite.x - checkpoint.x*32])
			if self.sprite.y < checkpoint.y*32:
				self.sprite.y += min([self.speed, checkpoint.y*32 - self.sprite.y])
			elif self.sprite.y > checkpoint.y*32:
				self.sprite.y -= min([self.speed, self.sprite.y - checkpoint.y*32])

class Boomb(Mob):
	def __init__(self, game, level, color):
		super(Boomb, self).__init__(game, level, "boomb.png", color)
		self.hp = 15 + 15 * level
		self.speed = 2

class Demon(Mob):
	def __init__(self, game, level, color):
		super(Demon, self).__init__(game, level, "demon.png", color)
		self.hp = 10 + 10 * level

class Slime(Mob):
	def __init__(self, game, level, color):
		super(Slime, self).__init__(game, level, "slime.png", color)
		self.hp = 10 + 10 * level

class Snake(Mob):
	def __init__(self, game, level, color):
		super(Snake, self).__init__(game, level, "snake.png", color)
		self.hp = 5 + 5 * level
		self.speed = 8

class Spider(Mob):
	def __init__(self, game, level, color):
		super(Spider, self).__init__(game, level, "spider.png", color)
		self.hp = 10 + 10 * level

class Virus(Mob):
	def __init__(self, game, level, color):
		super(Virus, self).__init__(game, level, "virus.png", color)
		self.hp = 10 + 10 * level
