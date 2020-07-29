import pyautogui as pg
import time
from typing import Tuple
from functools import wraps
from PIL import ImageChops
from positions import *

def has_changed(func) -> bool:
		@wraps(func)
		def wrapper(*args, **kwargs):
			time.sleep(0.5)
			pg.click(1000, 500)
			im_before = pg.screenshot(region=(0, 0, 1920, 700)).convert('RGB')
			func(*args, **kwargs)
			pg.click(1000, 500)
			im_after = pg.screenshot(region=(0, 0, 1920, 700)).convert('RGB')
			difference = ImageChops.difference(im_before, im_after)
			return difference.getbbox()

		return wrapper

class Clicker:
	def __init__(self, loop_through_primary: bool = True, loop_through_secondary: bool = True) -> None:
		self.loop_through_primary = loop_through_primary
		self.loop_through_secondary = loop_through_secondary
		self.bound_sign_position = pg.locateCenterOnScreen('assets/bound_sign.png')
		self.ok_button_position = None
		self.bottom_record_position = self.get_bottom_record_position()

	@staticmethod
	def get_bottom_record_position() -> Tuple[int, int]:
		bottom_columns = pg.locateOnScreen('assets/bottom_columns.png')
		x, y = pg.center(bottom_columns)
		return (x, y + bottom_columns.height)

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
		time.sleep(0.5)
		im = pg.screenshot()
		if im.getpixel(self.bottom_record_position) != (255, 255, 255):
			pg.click(self.bound_sign_position)

			time.sleep(1)

			if not self.ok_button_position:
				self.ok_button_position = pg.locateCenterOnScreen('assets/ok_button.png')

			pg.click(self.ok_button_position)

