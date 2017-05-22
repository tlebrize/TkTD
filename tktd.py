import pyglet, tkengine
from resources.menu import TitleScreen, Shop
from resources.game import Game

def main():
	window = tkengine.TkWindow(800, 600, caption="TkTD")
	world = tkengine.TkWorld(window)
	world.set_options((
		("money", 9999),
		("score", 0),
		("round", 0)
	))
	titlescreen = TitleScreen(world)
	game = Game(world)
	shop = Shop(world)
	world.add_scenes({"titlescreen": titlescreen, "game": game, "shop": shop})
	world.run("titlescreen")

if __name__ == "__main__":
	main()
