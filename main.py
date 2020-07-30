"""
Main module of the app resonsible for launching it.
"""

from clicker import Clicker
from prompt import Prompt

def main() -> None:
	"""Main function to run the app."""
	prompt = Prompt()
	prompt.greet()
	prompt.check_conditions()

	iterate_through_primary = prompt.iterate_through_primary()
	iterate_through_secondary = prompt.iterate_through_secondary()

	prompt.announce_start()
	
	clicker = Clicker(iterate_through_primary, iterate_through_secondary)
	clicker.run()


if __name__ == '__main__':
	main()
