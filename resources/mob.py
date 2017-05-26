import pyglet

class Mob(object):

	def __init__(self, level, cell, lib, batch):
		self.level = level
		self.hp = 5 + level * 5
		self.cell = cell
		self.next = cell.next
		self.lib = lib
		self.batch = batch
		image = lib.images.get("mob{}.png".format(level))
		self.sprite = pyglet.sprite.Sprite(image, x=cell.x * 32, y=cell.y * 32, batch=self.batch)

	def clear(self, dt, sprite):
		sprite.delete()

	def hit(self):
		self.hp -= 10
		hit_image = self.lib.images.get("hit.png")
		hit_sprite = pyglet.sprite.Sprite(hit_image,
					x=self.sprite.x, y=self.sprite.y, batch=self.batch)
		pyglet.clock.schedule_once(self.clear, 0.2, hit_sprite)

	def move(self):
		if self.sprite.x / 32 == self.next.x and self.sprite.y / 32 == self.next.y:
			self.cell = self.next
			self.next = self.cell.next
		if self.next and self.hp > 0:
			if self.cell.x < self.next.x:
				self.sprite.x += 4
			elif self.cell.x > self.next.x:
				self.sprite.x -= 4
			if self.cell.y < self.next.y:
				self.sprite.y += 4
			elif self.cell.y > self.next.y:
				self.sprite.y -= 4
			return True
		else:
			self.sprite.delete()
			return False
