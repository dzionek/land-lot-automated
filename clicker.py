"""
Module containing the Clicker class.
"""

import pyautogui as pg
from time import sleep
from typing import Optional

from positions import PRIMARY_UNIT_POSITION, SECONDARY_UNIT_POSITION, TERTIARY_UNIT_POSITION
from utils import has_changed


class Clicker:
	"""The class responsible for looping through each land lot unit and clicking accordingly to displayed data.

	Attributes:
		_loop_throuh_primary (bool):
			True if the Clicker should iterate through the primary area, false otherwise.
		_loop_throuh_secondary (bool):
			True if the Clicker should iterate through the secondary area, false otherwise.
		_bound_button_position (Tuple[int, int]):
			The coordinates of the button to bound land lot units.
		_ok_button_position (Optional[Tuple[int, int]]):
			The coordinates of the button to confirm the bounding.

	"""

	def __init__(self, loop_through_primary: bool = True, loop_through_secondary: bool = True) -> None:
		"""Construct the Clicker instance.

		Args:
			loop_through_primary: True if the Clicker should iterate through the primary area, false otherwise.
			loop_through_secondary: True if the Clicker should iterate through the secondary area, false otherwise.
		
		"""
		self._loop_through_primary = loop_through_primary
		self._loop_through_secondary = loop_through_secondary
		self._bound_button_position = pg.locateCenterOnScreen('assets/bound_sign.png')
		self._ok_button_position = None

	def run(self) -> None:
		"""Run the automated process (Clicker)."""
		self._loop_primary()

	def _loop_primary(self) -> None:
		"""Loop through the primary area and activate looping through the secondary one."""
		if self._loop_through_primary:
			is_different = True
			while is_different:
				self._loop_secondary()
				is_different = bool(Clicker._go_to_next('primary'))
		else:
			self._loop_secondary()

	def _loop_secondary(self) -> None:
		"""Loop through the secondary area and activate looping through the tertiary one."""
		if self._loop_through_secondary:
			is_different = True
			while is_different:
				self._loop_tertiary()
				is_different = bool(Clicker._go_to_next('secondary'))
		else:
			self._loop_tertiary()

	def _loop_tertiary(self) -> None:
		"""Loop through the tertiary area and bound the units inside each of them."""
		is_different = True
		while is_different:
			self._bound_units()
			is_different = bool(Clicker._go_to_next('tertiary'))

	@staticmethod
	@has_changed
	def _go_to_next(unit: str) -> None:
		"""Go to the next area of the given type.

		Args:
			unit: The type of area to be changed. Either 'primary', 'secondary', or 'tertiary'.
		
		Raises:
			ValueError: If the given unit is of different kind.
		
		"""
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

	def _bound_units(self) -> None:
		"""Bound the land lot units, if it is possible."""
		sleep(1)

		pg.click(self._bound_button_position)

		sleep(1.5)

		if not_found_center := pg.locateCenterOnScreen('assets/not_found.png'):
			pg.click(not_found_center)
			sleep(1)
		else:

			if not self._ok_button_position:
				self._ok_button_position = pg.locateCenterOnScreen('assets/ok_button.png')

			pg.click(self._ok_button_position)
