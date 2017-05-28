
import pyglet, os

class Graphics(object):

	def __init__(self, world):
		self.world = world
		self.images = {}
		self.sprites = []
		self.batches = [pyglet.graphics.Batch() for _ in range(3)]
		pyglet.gl.glClearColor(0.3, 0.6, 0.3, 0.0)
		for file in os.listdir("assets"):
			self.images.update({file: pyglet.image.load("assets/" + file)})

	def load_sprite(self, name, x=0, y=0, z=0, color=None):
		z = max(min(z, 2), 0)
		sprite = pyglet.sprite.Sprite(self.images.get(name), x=x, y=y,
			batch=self.batches[z])
		if color:
			sprite.color = color
		self.sprites.append(sprite)
		return sprite

	def draw(self):
		for batch in self.batches:
			batch.draw()
