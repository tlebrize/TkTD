import pyglet, tkengine, random, queue
from resources.sprite_lib import SpriteLib
from resources.cell import Cell
from resources.mob import Mob
from resources.objects import Tower, Checkpoint, Wall, Object

class GameScene(tkengine.TkScene):

	def __init__(self, world, Cell, lib):
		self.world = world
		self.size = 17
		self.lib = lib
		self.cells = []
		self.batch = pyglet.graphics.Batch()
		self.x = 0
		self.y = 0
		self.towers = []
		for x in range(0, self.size):
			line = []
			for y in range(0, self.size):
				line.append(Cell(x, y, self.lib, self.batch))
			self.cells.append(line)
		self.running = False
		self.current = None
		self.init_cells()
		self.move_cursor(self.x ,self.y)
		self.key_handlers = {
			pyglet.window.key.ESCAPE	: pyglet.app.exit,
			pyglet.window.key.BACKSPACE	: self.destroy,
			pyglet.window.key.SPACE		: self.build,
			pyglet.window.key.RETURN	: self.finish,
			pyglet.window.key.RIGHT		: lambda : self.move_cursor(1, 0),
			pyglet.window.key.LEFT		: lambda : self.move_cursor(-1, 0),
			pyglet.window.key.DOWN		: lambda : self.move_cursor(0, -1),
			pyglet.window.key.UP		: lambda : self.move_cursor(0, 1),
		}
		self.start = self.cells[14][2]
		self.end = self.cells[2][14]
		self.start.content = Checkpoint(None, 14, 2, self.lib, self.batch)
		self.end.content = Checkpoint(self.start, 2, 14, self.lib, self.batch)
		self.build_paths()
		self.temporary = []
		self.mob_level = -1
		pyglet.clock.schedule_interval(self.draw, 1 / 60)
		self.running = False

	def build_paths(self):
		for line in self.cells:
			for cell in line:
				cell.next = None
				cell.delete_effect("dot.png")
		frontier = queue.Queue()
		frontier.put(self.end)
		visited = [self.end]
		while not frontier.empty():
			current = frontier.get()
			if not isinstance(current, Object):
				for node in current.neighbors.values():
					if node not in visited:
						if not isinstance(node.content, Object):
							frontier.put(node)
							node.next = current
						visited.append(node)
		if self.start in visited:
			node = self.start
			while node is not self.end:
				node.add_effect("dot.png")
				node = node.next
		return self.start in visited

	def init_cells(self):
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].neighbors = {
					"E": self.cells[(x - 1) % self.size][y],
					"W": self.cells[(x + 1) % self.size][y],
					"S": self.cells[x][(y - 1) % self.size],
					"N": self.cells[x][(y + 1) % self.size]
				}
				if x == 0 or y == 0 or x == self.size-1 or y == self.size-1:
					self.cells[x][y].content = Wall(x, y, self.lib, self.batch)

	def move_cursor(self, x, y):
		if self.current:
			self.current.delete_effect("selected.png")
		self.x = (self.x + x) % self.size
		self.y = (self.y + y) % self.size
		self.current = self.cells[self.x][self.y]
		self.current.add_effect("selected.png")

	def draw(self, _):
		self.world.window.clear()
		self.batch.draw()

	def destroy(self):
		if self.running != False:
			return
		if self.current.content == None:
			return
		if self.current in self.temporary:
			return
		if isinstance(self.current.content, Tower):
			self.current.delete_tower()
			self.build_paths()

	def build(self):
		if len(self.temporary) < 5 and self.current.content == None and not self.running:
			kind = "t0.{}.png".format(random.randint(0, 2))
			self.current.add_tower(kind)
			self.current.add_effect("temporary.png")
			self.temporary.append(self.current)
			if not self.build_paths():
				self.current.delete_tower()
				self.current.delete_effect("temporary.png")
				self.temporary.remove(self.current)

	def mob_turn(self, _):
		for mob in self.mobs:
			if not mob.move():
				self.mobs.remove(mob)
		if self.mob_sent < 100:
			if self.mob_sent % 10 == 0:
				self.mobs.append(Mob(self.mob_level, self.start, self.lib, self.batch))
			self.mob_sent += 1
		if len(self.mobs) == 0:
			for tower in self.towers:
				tower.running = False
			self.running = False
			pyglet.clock.unschedule(self.mob_turn)
			self.build_paths()

	def finish(self):
		if self.current not in self.temporary:
			return
		self.towers.append(self.current.content)
		self.running = True
		for cell in self.temporary:
			cell.delete_effect("temporary.png")
		self.temporary.remove(self.current)
		for cell in self.temporary:
			cell.content.set_sprite("rock.png")
		self.temporary = []
		self.build_paths()
		self.mobs = []
		self.mob_sent = 0
		self.mob_level = (self.mob_level + 1) % 3
		pyglet.clock.schedule_interval(self.mob_turn, 1/30)
		for line in self.cells:
			for cell in line:
				cell.delete_effect("dot.png")
		for tower in self.towers:
			tower.running = True
			tower.play(mobs=self.mobs)


def main():
	window = tkengine.TkWindow(544, 544)
	pyglet.gl.glClearColor(0.3, 0.6, 0.3, 0.0)
	world = tkengine.TkWorld(window)
	lib = SpriteLib("assets")
	game = GameScene(world, Cell, lib=lib)
	world.add_scenes({"game": game})
	world.run("game")

if __name__ == "__main__":
	main()
