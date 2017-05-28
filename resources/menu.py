import pyglet

class Menu(object):


	def __init__(self, game):
		self.game = game
		self.world = game.world
		self.batch = pyglet.graphics.Batch()

		self.hp = game.hp
		self.current = self.game.grid.current.content

		self.labels = {
			"hp": pyglet.text.Label("HP : {}".format(self.hp),
					x=682, y=655, batch=self.batch),
			"current": pyglet.text.Label(str(self.current),
					x=682, y=635, batch=self.batch),
			"mob": pyglet.text.Label("", x=682, y=615, batch=self.batch)
		}


	def update_mob(self, mob):
		self.labels["mob"].text = mob.__name__

	def draw(self):
		if self.hp != self.game.hp:
			self.labels["hp"].text = "HP : {}".format(self.game.hp)
			self.hp = self.game.hp
		if self.current != self.game.grid.current.content:
			self.labels["current"].text = str(self.game.grid.current.content)
			self.current = self.game.grid.current.content
		for label in self.labels.values():
			label.draw()

