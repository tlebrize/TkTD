import pyglet, os

class SpriteLib(object):

	def __init__(self, path):
		self.images = {}
		for file in os.listdir(path):
			self.images.update({file: pyglet.image.load(path + '/' + file)})
