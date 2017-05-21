import pyglet, tkengine

class TitleScreen(tkengine.TkMenu):
	
	def __init__(self, world):
		super(TitleScreen, self).__init__(world, label="TkTD", menu_items=(
			("Start"	, lambda: self.world.transition("game")),
			("Quit"		, lambda: self._quit())
		))

	def entry(self):
		self.world.window.set_caption("TkTD")
		pyglet.gl.glClearColor(0.2, 0.2, 0.2, 0)
		self.world.window.set_size(600, 600)
		self.world.window.center()


class Cell(tkengine.TkPlainCell):

	COLOR = {
		True: {"empty": (0.64, 0.64, 0.64), "basic": (0.14, 0.14, 0.14),"fire": (0.75, 0.14, 0.14)},
		False: {"empty": (0.74, 0.74, 0.74), "basic": (0.34, 0.34, 0.34),"fire": (0.95, 0.34, 0.34)}
	}

	KINDS = ["empty", "basic", "fire"]

	def __init__(self, x, y, scale):
		super(Cell, self).__init__(x, y, scale)
		self.selected
		self.kind = "empty"
		self.color = Cell.COLOR[self.selected][self.kind]

	def draw(self):
		self.color = Cell.COLOR[self.selected][self.kind]
		super(Cell, self).draw()

	def build(self, kind):
		if kind in Cell.KINDS:
			self.kind = kind


class Game(tkengine.TkGridMap):

	BUILD, PLAY, SCORE = range(3)

	def __init__(self, world):
		super(Game, self).__init__(world, Cell)
		self.key_handlers.update({
			pyglet.window.key.RETURN : self.select,
			pyglet.window.key.ESCAPE : self.back
		})

	def back(self):
		self.world.transition("titlescreen")

	def select(self):
		self.world.transition("shop", current=self.current)


class Shop(tkengine.TkMenu):

	def __init__(self, world):
		super(Shop, self).__init__(world, label="Tower Shop", menu_items=(
			("Normal [50]"	, lambda: self.build("basic")),
			("Fire   [150]"	, lambda: self.build("fire")),
			("Back"			, self.back)
		))
		self.current = None

	def entry(self, current):
		self.current = current

	def build(self, kind):
		self.current.build(kind)
		self.world.transition("game")

	def back(self):
		self.current = None
		self.world.transition("game")


def main():
	window = tkengine.TkWindow(caption="TkTD")
	world = tkengine.TkWorld(window)
	titlescreen = TitleScreen(world)
	game = Game(world)
	shop = Shop(world)
	world.add_scenes({"titlescreen": titlescreen, "game": game, "shop": shop})
	world.run("titlescreen")

if __name__ == "__main__":
	main()