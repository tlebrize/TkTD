import pyglet

class Checkpoint(object):

	def __init__(self, next, x, y, lib, batch):
		self.next = next
		self.x = x
		self.y = y
		self.lib = lib
		self.batch = batch
		image = self.lib.images.get("check.png")
		self.sprite = pyglet.sprite.Sprite(image,
			x=self.x * 32, y=self.y * 32, batch=self.batch)
