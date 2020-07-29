"""
Main module of the app, running it.
"""

from clicker import Clicker

def main():
	clicker = Clicker(False, True)
	clicker.run()


if __name__ == '__main__':
	main()
