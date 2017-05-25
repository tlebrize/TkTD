import pyglet, tkengine, os, random, queue

class GameScene(tkengine.TkScene):

	def __init__(self, world, Cell, lib):
		self.world = world
		self.size = 15
		self.lib = lib
		self.cells = []
		self.batch = pyglet.graphics.Batch()
		self.x = 0
		self.y = 0
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
		self.start = self.cells[2][2]
		self.end = self.cells[12][12]
		self.start.content = Checkpoint("start.png", None, 2, 2, lib, self.batch)
		self.end.content = Checkpoint("end.png", self.start, 12, 12, lib, self.batch)
		self.build_paths()
		self.temporary = []
		self.mob_level = -1
		pyglet.clock.schedule_interval(self.draw, 1 / 60)

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
			if not isinstance(current, Tower):
				for node in current.neighbors.values():
					if node not in visited:
						if not isinstance(node.content, Tower):
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
		if self.current.content == None:
			return
		if self.current in self.temporary:
			return
		if isinstance(self.current.content, Tower):
			self.current.delete_tower()
			self.build_paths()

	def build(self):
		if len(self.temporary) < 5 and self.current.content == None:
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
		if self.mob_sent < 10:
			if self.mob_sent % 2 == 0:
				self.mobs.append(Mob(self.mob_level, self.start, self.lib, self.batch))
			self.mob_sent += 1
		if len(self.mobs) == 0:
			pyglet.clock.unschedule(self.mob_turn)

	def finish(self):
		if self.current not in self.temporary:
			return
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
		pyglet.clock.schedule_interval(self.mob_turn, 0.5)

class Cell(object):

	def __init__(self, x, y, lib, batch):
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		self.neighbors = {}
		self.color = (0.2, 0.2, 0.2)
		self.effects = {}
		self.content = None
		self.next = None

	def add_effect(self, name):
		if not self.effects.get(name):
			image = self.lib.images.get(name)
			sprite = pyglet.sprite.Sprite(image, batch=self.batch)
			sprite.x = self.x * 32
			sprite.y = self.y * 32
			self.effects.update({name: sprite})

	def delete_effect(self, name=False):
		if not name:
			for sprite in self.effects:
				self.effects.get(sprite).delete()
			self.effects = {}
		elif self.effects.get(name):
			self.effects.get(name).delete()
			self.effects.pop(name)

	def select(self):
		self.add_effect("selected.png")

	def deselect(self):
		self.delete_effect("selected.png")

	def add_tower(self, name):
		if self.content == None:
			self.content = Tower(name, self.x, self.y, self.lib, self.batch)

	def delete_tower(self):
		if isinstance(self.content, Tower):
			self.content.sprite.delete()
			self.content = None

class Tower(object):

	def __init__(self, name, x, y, lib, batch):
		self.x = x
		self.y = y
		self.name = name
		self.lib = lib
		self.batch = batch
		self.sprite = None
		self.set_sprite(self.name)

	def set_sprite(self, name):
		if self.sprite:
			self.sprite.delete()
		self.name = name
		image = self.lib.images.get(self.name)
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)

class Checkpoint(object):
	def __init__(self, name, next, x, y, lib, batch):
		self.name = name
		self.next = next
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		image = self.lib.images.get(self.name)
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)

class SpriteLib(object):

	def __init__(self, path):
		self.images = {}
		for file in os.listdir(path):
			self.images.update({file: pyglet.image.load(path + '/' + file)})

class Mob(object):

	def __init__(self, level, cell, lib, batch):
		self.level = level
		self.cell = cell
		self.lib = lib
		self.batch = batch
		image = lib.images.get("mob{}.png".format(level))
		self.sprite = pyglet.sprite.Sprite(image, x=cell.x * 32, y=cell.y * 32, batch=self.batch)

	def move(self):
		if self.cell.next:
			self.cell = self.cell.next
			self.sprite.x = self.cell.x * 32
			self.sprite.y = self.cell.y * 32
			return True
		else:
			self.sprite.delete()
			return False

def main():
	window = tkengine.TkWindow(480, 480)
	pyglet.gl.glClearColor(0.3, 0.6, 0.3, 0.0)
	world = tkengine.TkWorld(window)
	lib = SpriteLib("assets")
	game = GameScene(world, Cell, lib=lib)
	world.add_scenes({"game": game})
	world.run("game")

if __name__ == "__main__":
	main()