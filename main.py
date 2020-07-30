"""
Main module of the app resonsible for launching it.
"""

from clicker import Clicker

def main() -> None:
	"""Main function to run the app."""
	clicker = Clicker(False, False)
	clicker.run()


if __name__ == '__main__':
	main()
