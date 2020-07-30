import pyautogui as pg
import time
from typing import Tuple, Callable, Optional
from functools import wraps
from PIL import ImageChops
from positions import *

def has_changed(func: Callable) -> Callable:
	"""Decorator to see if anything has changed in the frame with land lot units.

	Args:
		func: The function to be decorated.

	Returns:
		The wrapper with the decorated function.

	"""
	@wraps(func)
	def wrapper(*args, **kwargs) -> Tuple[int, int, int, int]:
		"""The wrapper of the decorator."""
		time.sleep(1)
		pg.click(1000, 500)
		im_before = pg.screenshot(region=DROPDOWNS_REGION).convert('RGB')
		func(*args, **kwargs)
		pg.click(1000, 500)
		im_after = pg.screenshot(region=DROPDOWNS_REGION).convert('RGB')
		difference = ImageChops.difference(im_before, im_after)
		return difference.getbbox()

	return wrapper

class Clicker:
	def __init__(self, loop_through_primary: bool = True, loop_through_secondary: bool = True) -> None:
		self.loop_through_primary = loop_through_primary
		self.loop_through_secondary = loop_through_secondary
		self.bound_sign_position = pg.locateCenterOnScreen('assets/bound_sign.png')
		self.ok_button_position = None

	def run(self) -> None:
		self.loop_primary()

	def loop_primary(self) -> None:
		if self.loop_through_primary:
			while True:
				self.loop_secondary()
				is_different = Clicker.go_to_next('primary')
				if not is_different:
					break
		else:
			self.loop_secondary()

	def loop_secondary(self) -> None:
		if self.loop_through_secondary:
			while True:
				self.loop_tertiary()
				is_different = Clicker.go_to_next('secondary')
				if not is_different:
					break
		else:
			self.loop_tertiary()

	def loop_tertiary(self) -> None:
		while True:
			self.bound_units()
			is_different = Clicker.go_to_next('tertiary')
			if not is_different:
				break

	@staticmethod
	@has_changed
	def go_to_next(unit: str) -> None:
		if unit == 'primary':
			unit_position = PRIMARY_UNIT_POSITION
		elif unit == 'secondary':
			unit_position = SECONDARY_UNIT_POSITION
		elif unit == 'tertiary':
			unit_position = TERTIARY_UNIT_POSITION
		else:
			raise ValueError(f'The given unit is invalid: {unit}.')

		pg.click(unit_position)
		pg.press('down')
		pg.press('enter')

	def bound_units(self) -> None:
		time.sleep(1)

		pg.click(self.bound_sign_position)

		time.sleep(1.5)

		if not_found_center := pg.locateCenterOnScreen('assets/not_found.png'):
			pg.click(not_found_center)
			time.sleep(1)
		else:

			if not self.ok_button_position:
				self.ok_button_position = pg.locateCenterOnScreen('assets/ok_button.png')

			pg.click(self.ok_button_position)
