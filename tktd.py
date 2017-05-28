import tkengine, pyglet
from resources.game import Game

def main():
	window = tkengine.TkWindow(1024, 672)
	world = tkengine.TkWorld(window)
	game = Game(world)
	world.add_scenes({"game": game})
	world.run("game")

if __name__ == "__main__":
	main()