import pyautogui as pg
import time
from positions import *

class Clicker:
	def __init__(self, loop_through_primary: bool = True, loop_through_secondary: bool = True):
		self.loop_through_primary = loop_through_primary
		self.loop_through_secondary = loop_through_secondary
		self.bound_sign_position = pg.locateCenterOnScreen('assets/bound_sign.png')
		self.ok_button_position = None
		self.bottom_record_position = self.get_bottom_record_position()

	@staticmethod
	def get_bottom_record_position():
		bottom_columns = pg.locateOnScreen('assets/bottom_columns.png')
		x, y = pg.center(bottom_columns)
		return (x, y + bottom_columns.height)


	def loop_primary(self):
		if self.loop_through_primary:
			for _ in range(5):
				self.loop_secondary()
				next('primary')
		else:
			self.loop_secondary()

	def loop_secondary(self):
		if self.loop_through_secondary:
			for _ in range(5):
				loop_tertiary()
				next('secondary')
		else:
			loop_tertiary()

	@staticmethod
	def loop_tertiary():
		for _ in range(5):
			next('tertiary')

	@staticmethod
	def next(unit: str):
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

	def bound_units(self):
		im = pg.screenshot()
		if im.getpixel(self.bottom_record_position) != (255, 255, 255):
			pg.click(self.bound_sign_position)

			time.sleep(1)

			if not self.ok_button_position:
				self.ok_button_position = pg.locateCenterOnScreen('assets/ok_button.png')

			pg.click(self.ok_button_position)
