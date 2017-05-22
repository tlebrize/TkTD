import tkengine, pyglet
from .units import Ling

class Cell(tkengine.TkPlainCell):

	COLOR = {
		True: {"empty": (0.35, 0.35, 0.7), "basic": (0.15, 0.15, 0.5),
			"fire": (0.70, 0.15, 0.5), "wall": (0.05, 0.05, 0.5)},
		False: {"empty": (0.9, 0.9, 0.9), "basic": (0.15, 0.15, 0.15),
			"fire": (0.70, 0.15, 0.15), "wall": (0.05, 0.05, 0.1)}
	}

	KINDS = ["empty", "basic", "fire", "wall"]

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

	def __init__(self, world):
		super(Game, self).__init__(world, Cell, size=17, scale=3)
		self.running = False
		self.key_handlers.update({
			pyglet.window.key.ESCAPE : self.back})
		self.text_batch = pyglet.graphics.Batch()
		pyglet.text.Label("Money:", font_size=24, batch=self.text_batch,
			x=600, y=560)
		pyglet.text.Label("Score:", font_size=24, batch=self.text_batch,
			x=600, y=460)
		pyglet.text.Label("Round:", font_size=24, batch=self.text_batch,
			x=600, y=360)
		self.tip = pyglet.text.Label("Space to start.", font_size=18,
			batch=self.text_batch, x=600, y=60)
		self.units = [Ling(world, x * 100, 600) for x in range(0, 6)]


	def entry(self):
		if self.running:
			self.attack_phase()
		else:
			self.build_phase()

	def exit(self):
		pyglet.clock.unschedule(self.update)

	def draw(self, _):
		super(Game, self).draw(_)
		text_list = []
		text_list.append(pyglet.text.Label(str(self.world.money), font_size=24,
			batch=self.text_batch, x=620, y=510))
		text_list.append(pyglet.text.Label(str(self.world.score), font_size=24,
			batch=self.text_batch, x=620, y=410))
		text_list.append(pyglet.text.Label(str(self.world.round), font_size=24,
			batch=self.text_batch, x=620, y=310))
		self.text_batch.draw()
		for text in text_list:
			text.delete()
		for unit in self.units:
			unit.draw()

	def update(self, _):
		for unit in self.units:
			unit.update()

	def build_phase(self):
		pyglet.clock.unschedule(self.update)
		self.key_handlers.update({
			pyglet.window.key.RETURN : self.select,
			pyglet.window.key.SPACE : self.attack_phase,
		})
		self.tip.delete()
		self.tip = pyglet.text.Label("Space to start.", font_size=18,
			batch=self.text_batch, x=600, y=60)
		self.running = False

	def attack_phase(self):
		pyglet.clock.schedule_interval(self.update, 1 / 60)
		self.key_handlers.update({
			pyglet.window.key.RETURN : lambda: None,
			pyglet.window.key.SPACE : self.pause
		})
		self.tip.delete()
		self.tip = pyglet.text.Label("Attack started !!", font_size=18,
				batch=self.text_batch, x=600, y=60)
		self.running = True

	def pause(self):
		self.running = not self.running

	def back(self):
		self.world.transition("titlescreen")

	def select(self):
		self.world.transition("shop", current=self.current)

