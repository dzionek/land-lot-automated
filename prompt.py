"""
Module containing the Prompt class.
"""

import pyautogui as pg

class Prompt:
	"""The class responsible for validating the initial conditions before the Clicker will start to work."""

	def __init__(self, validate_fullscreen: bool = True, validate_record: bool = True) -> None:
		self._validate_fullscreen = validate_fullscreen
		self._validate_record = validate_record

	@staticmethod
	def check_exit(button: str) -> None:
		if button == 'Anuluj':
			exit()

	@staticmethod
	def greet() -> None:
		button = pg.confirm(
			text='Witaj w programie Land Lot Automated, który służy do automatyzacji'
			+ ' pozyskiwania powiązania jednostki rejestrowej gruntowej z lokalową w programie TurboEWID.',
			title='Land Lot Automated', buttons=['Dalej', 'Anuluj']
		)
		Prompt.check_exit(button)

	@staticmethod
	def announce_start() -> None:
		button = pg.confirm(
			text='Po kliknięciu "Start" program rozpocznie działanie.',
			title='Land Lot Automated', buttons=['Start', 'Anuluj']
		)
		Prompt.check_exit(button)

	def check_conditions(self) -> None:
		button = pg.confirm(
			text='Upewnij się, że masz włączony program TurboEWID, a w nim rejestr lokali,'
				+ ' który ustawiony jest w trybie pełnoekranowym.'
				+ ' Gdy będziesz gotowy/a, kliknij OK.',
			title='Land Lot Automated', buttons=['OK', 'Anuluj']
		)

		Prompt.check_exit(button)

		validation_unsuccessfull = not(self._validate())
		while validation_unsuccessfull:
			button = pg.confirm(
				text='Niestety, ale twoje ustawienie jest nieprawidłowe!' 
					+ ' Upewnij się, że masz włączony program TurboEWID, a w nim rejestr lokali,'
				 	+ ' który ustawiony jest w trybie pełnoekranowym. Gdy będziesz gotowy/a, kliknij OK.',
				title='Land Lot Automated', buttons=['OK', 'Anuluj']
			)

			Prompt.check_exit(button)

			validation_unsuccessfull = not(self._validate())

	@staticmethod
	def iterate_through_primary() -> bool:
		button: str = pg.confirm(
			text='Czy mam przejść przez wszystkie jednostki ewidencyjne?',
			title='Land Lot Automated', buttons=['Tak', 'Nie']
		)

		return button == 'Tak'

	@staticmethod
	def iterate_through_secondary() -> bool:
		button: str = pg.confirm(
			text='Czy mam przejść przez wszystkie obręby ewidencyjne?',
			title='Land Lot Automated', buttons=['Tak', 'Nie']
		)

		return button == 'Tak'

	def _validate(self) -> bool:
		is_valid = True

		if self._validate_fullscreen:
			is_valid = is_valid and Prompt._is_valid_fullscreen()
		if self._validate_record:
			is_valid = is_valid and Prompt._is_valid_record()

		return is_valid

	@staticmethod
	def _is_valid_fullscreen() -> bool:
		return bool(pg.locateOnScreen('assets/validator_fullscreen.png', confidence=0.9))

	@staticmethod
	def _is_valid_record() -> bool:
		return bool(pg.locateOnScreen('assets/validator_record.png', confidence=0.9))
