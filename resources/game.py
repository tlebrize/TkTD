import tkengine, pyglet, random
from .grid import Grid
from .graphics import Graphics
from .mob import Mob
from .tower import Rock
from .chipped import *
from .mob import *
from .menu import Menu

class Game(tkengine.TkScene):


	def __init__(self, world):
		self.world = world
		self.hp = 10
		self.level = -1
		self.running = False
		self.graphics = Graphics(world)
		self.grid = Grid(self.graphics, 21)
		self.menu = Menu(self)
		self._setup_checkpoints()
		self.grid.build_paths(self.checkpoints)
		self.temporary = []
		self.mobs = []
		self.towers = []
		self.checkpoint = 0
		self.grid.current.add_effect("selected.png")
		self.key_handlers = {
			pyglet.window.key.ESCAPE	: pyglet.app.exit,
			pyglet.window.key.SPACE		: self._build,
			pyglet.window.key.BACKSPACE	: self._destroy,
			pyglet.window.key.RETURN	: self._finish,
			pyglet.window.key.LEFT		: lambda : self.grid.move_cursor(-1, 0),
			pyglet.window.key.UP		: lambda : self.grid.move_cursor(0, 1),
			pyglet.window.key.RIGHT		: lambda : self.grid.move_cursor(1, 0),
			pyglet.window.key.DOWN		: lambda : self.grid.move_cursor(0, -1),
		}
		pyglet.clock.schedule_interval(self._draw, 1 / 60)

	def _draw(self, _):
		self.world.window.clear()
		self.graphics.draw()
		self.menu.draw()


	def _destroy(self):
		if isinstance(self.grid.current.content, Tower) and not self.running and \
				self.grid.current not in self.temporary:
			if self.grid.current.content in self.towers:
				self.towers.remove(self.grid.current.content)
			self.grid.current.content.sprite.delete()
			self.grid.current.walkable = True
			self.grid.current.content = None


	def _finish(self):
		if self.running or self.grid.current not in self.temporary:
			return
		self.towers.append(self.grid.current.content)
		self.grid.current.delete_effect("temporary.png")
		self.temporary.remove(self.grid.current)
		for tower in self.temporary:
			tower.content.sprite.delete()
			tower.content = Rock(tower.x*32, tower.y*32, self.graphics)
			tower.delete_effect("temporary.png")
		self.temporary = []
		self._start_level()


	def _build(self):
		if self.running or len(self.temporary) >= 5 or not self.grid.current.walkable or \
					self.grid.current in self.checkpoints:
			return
		self.grid.current.walkable = False
		if not self.grid.build_paths(self.checkpoints):
			self.grid.current.walkable = True
			return
		quality = random.choice(["Chipped"])
		color = random.choice(["Aquamarine","Emerald","Opal","Saphire","Diamond","Topaz","Amethyst","Ruby"])
		x = self.grid.current.x * 32
		y = self.grid.current.y * 32
		tower = globals().get(quality+"_"+color)
		self.grid.current.content = tower(x, y, self, self.graphics)
		self.grid.current.add_effect("temporary.png")
		self.temporary.append(self.grid.current)


	# def _follow(self):
	# 	self.grid.current.delete_effect("selected.png")
	# 	while self.checkpoint < len(self.checkpoints) - 1 and not self.grid.current.next[self.checkpoint]:
	# 		self.checkpoint += 1
	# 	if self.checkpoint == len(self.checkpoints) - 1:
	# 		self.grid.current.add_effect("selected.png")
	# 	elif not self.grid.current.next[self.checkpoint]:
	# 		raise Exception("Invalid path.")
	# 	else:
	# 		self.grid.current = self.grid.current.next[self.checkpoint]
	# 		self.grid.current.add_effect("selected.png")


	def _send_mob(self, _, mob):
		self.mobs.append(mob(self, self.level, self.mob_color))


	def _stop(self, _):
		if len(self.mobs) == 0:
			self.running = False
		else:
			pyglet.clock.schedule_once(self._stop, 0.5)


	def _start_level(self):
		self.level += 1
		self.running = True
		self.mob_color = self.level // 7
		mob = [Slime, Spider, Demon, Angel, Boomb, Snake, Virus][self.level % 7]
		self.menu.update_mob(mob)
		pyglet.clock.schedule_interval(self._send_mob, 0.5, mob)
		pyglet.clock.schedule_once(lambda _:pyglet.clock.unschedule(self._send_mob), 5.1)
		pyglet.clock.schedule_once(self._stop, 5.1)
		for tower in self.towers:
			tower.play()


	def _setup_checkpoints(self):
		start = self.grid.cells[1][1]
		mid = self.grid.cells[10][10]
		end = self.grid.cells[19][19]
		start.sprite = self.graphics.load_sprite("check.png", 1*32, 1*32, 0)
		mid.sprite = self.graphics.load_sprite("check.png", 10*32, 10*32, 0)
		end.sprite = self.graphics.load_sprite("check.png", 19*32, 19*32, 0)
		self.checkpoints = [start, mid, end]



