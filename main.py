"""
Main module of the app, running it.
"""

from clicker import Clicker

def main():
	clicker = Clicker(False, False)
	clicker.bound_units()


if __name__ == '__main__':
	main()
