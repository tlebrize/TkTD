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

	COLORS = {
		"empty": [0.9, 0.9, 0.9],
		"wall": [0.3, 0.3, 0.3],
		"turret": [0.6, 0.6, 0.6]
	}

	KINDS = ["empty", "turret", "wall"]

	def __init__(self, x, y, scale):
		super(Cell, self).__init__(x, y, scale)
		self.kind = "empty"
		self.color = self.get_color()

	def get_color(self):
		color = Cell.COLORS.get(self.kind)
		if self.selected:
			color[1] *= 0.5
			color[0] *= 0.5
		return color

	def draw(self):
		self.color = self.get_color()
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
			("Turret [50]"	, lambda: self.build("turret")),
			("Wall   [5]"	, lambda: self.build("wall")),
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