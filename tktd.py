import pyglet, tkengine, os, random

class GameScene(tkengine.TkScene):

	def __init__(self, world, Cell, lib):
		self.world = world
		self.size = 15
		self.cells = []
		self.batch = pyglet.graphics.Batch()
		self.x = 0
		self.y = 0
		for x in range(0, self.size):
			line = []
			for y in range(0, self.size):
				line.append(Cell(x, y, lib=lib, batch=self.batch))
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
		self.cells[0][14].add_sprite("start.png")
		self.cells[7][7].add_sprite("end.png")
		self.cells[0][14].kind = Cell.CHECKPOINT
		self.cells[7][7].kind = Cell.CHECKPOINT
		self.cells[5][5].add_sprite("mob1.png")
		self.cells[5][6].add_sprite("mob2.png")
		self.cells[5][7].add_sprite("mob3.png")
		self.temporary = []
		pyglet.clock.schedule_interval(self.draw, 1 / 60)

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
			self.current.deselect()
		self.x = (self.x + x) % self.size
		self.y = (self.y + y) % self.size
		self.current = self.cells[self.x][self.y]
		self.current.select()

	def draw(self, _):
		self.world.window.clear()
		self.batch.draw()

	def destroy(self):
		if self.current.kind == Cell.TOWER:
			self.current.kind = Cell.EMPTY
			self.current.delete_sprite()
			if self.current in self.temporary:
				self.temporary.remove(self.current)
			self.current.add_sprite("selected.png")

	def build(self):
		if len(self.temporary) < 5 and self.current.kind == Cell.EMPTY:
			kind = "t0.{}.png".format(random.randint(0, 2))
			self.current.add_sprite(kind)
			self.current.add_sprite("temporary.png")
			self.temporary.append(self.current)
			self.current.kind = Cell.TOWER

	def finish(self):
		if self.current in self.temporary:
			for cell in self.temporary:
				cell.delete_sprite("temporary.png")
			self.temporary.remove(self.current)
			for cell in self.temporary:
				cell.delete_sprite()
				cell.add_sprite("rock.png")
			self.temporary = []

class Cell(object):

	EMPTY, CHECKPOINT, TOWER = range(3)

	def __init__(self, x, y, lib=None, batch=None):
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		self.selected = False
		self.neighbors = {}
		self.color = (0.2, 0.2, 0.2)
		self.sprites = {}
		self.kind = Cell.EMPTY

	def add_sprite(self, name):
		if not self.sprites.get(name):
			image = self.lib.images.get(name)
			sprite = pyglet.sprite.Sprite(image, batch=self.batch)
			sprite.x = self.x * 32
			sprite.y = self.y * 32
			self.sprites.update({name: sprite})

	def delete_sprite(self, name=False):
		if not name:
			for sprite in self.sprites:
				self.sprites.get(sprite).delete()
			self.sprites = {}
		elif self.sprites.get(name):
			self.sprites.get(name).delete()
			self.sprites.pop(name)

	def select(self):
		self.selected = True
		self.add_sprite("selected.png")

	def deselect(self):
		if self.selected:
			self.selected = False
			self.delete_sprite("selected.png")

class SpriteLib(object):

	def __init__(self, path):
		self.images = {}
		for file in os.listdir(path):
			self.images.update({file: pyglet.image.load(path + '/' + file)})

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