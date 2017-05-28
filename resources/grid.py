import queue
from .cell import Cell

class Grid(object):

	def __init__(self, graphics, size):
		self.graphics = graphics
		self.size = size
		self.cells = []
		for x in range(self.size):
			line = []
			for y in range(self.size):
				line.append(Cell(x, y, self.graphics))
			self.cells.append(line)
		self.x = 1
		self.y = 1
		self.current = self.cells[self.x][self.y]
		self._init_neighbors()

	def move_cursor(self, x, y):
		if self.current:
			self.current.delete_effect("selected.png")
		self.x = (self.x + x) % self.size
		self.y = (self.y + y) % self.size
		self.current = self.cells[self.x][self.y]
		self.current.add_effect("selected.png")

	def build_paths(self, checkpoints):
		for line in self.cells:
			for cell in line:
				cell.next = [None for _ in range(len(checkpoints))]
				cell.delete_effect("dot.png")
		for i in range(len(checkpoints) - 1):
			end = checkpoints[i]
			start = checkpoints[i+1]
			frontier = queue.Queue()
			frontier.put(start)
			visited = [start]
			while not frontier.empty():
				current = frontier.get()
				for node in current.neighbors.values():
					if node not in visited:
						if node.walkable:
							frontier.put(node)
							node.next[i] = current
						visited.append(node)
			if end in visited:
				node = end.next[i]
				while node is not start:
					node.add_effect("dot.png", z=0)
					node = node.next[i]
			else:
				return False
		return True

	def _init_neighbors(self):
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].neighbors = {
					"E": self.cells[(x - 1) % self.size][y],
					"W": self.cells[(x + 1) % self.size][y],
					"S": self.cells[x][(y - 1) % self.size],
					"N": self.cells[x][(y + 1) % self.size]
				}
				if x == 0 or y == 0 or x == self.size-1 or y == self.size-1:
					self.cells[x][y].walkable = False
					self.cells[x][y].sprite = self.graphics.load_sprite("wall.png",
						x=x*32, y=y*32)

