"""
Main module of the app, running it.
"""

from clicker import Clicker

def main() -> None:
	clicker = Clicker(False, False)
	clicker.run()


if __name__ == '__main__':
	main()
