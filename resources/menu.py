import pyglet, tkengine

class TitleScreen(tkengine.TkMenu):

	def __init__(self, world):
		super(TitleScreen, self).__init__(world, label="TkTD", menu_items=(
			("Start"	, lambda: self.world.transition("game")),
			("Quit"		, lambda: self._quit())
		))
		self.world.window.set_caption("TkTD")
		pyglet.gl.glClearColor(0.2, 0.2, 0.2, 0)
		self.world.window.center()


class Shop(tkengine.TkMenu):

	ITEMS = {"wall": 5, "basic": 50, "fire": 150}

	def __init__(self, world):
		super(Shop, self).__init__(world, label="Tower Shop", menu_items=(
			("Wall   [5]"	, lambda: self.build("wall")),
			("Normal [50]"	, lambda: self.build("basic")),
			("Fire   [150]"	, lambda: self.build("fire")),
			("Back"			, self.back)
		))
		self.current = None

	def entry(self, current):
		self.current = current

	def build(self, kind):
		if self.world.money > Shop.ITEMS.get(kind):
			self.current.build(kind)
			self.world.money -= Shop.ITEMS.get(kind)
		self.world.transition("game")

	def back(self):
		self.current = None
		self.world.transition("game")

