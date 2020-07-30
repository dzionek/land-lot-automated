from typing import Tuple, Callable, Any, Optional
from functools import wraps
from PIL import ImageChops
from time import sleep
import pyautogui as pg

from positions import CENTER_POSITION

def has_changed(func: Callable) -> Callable:
	"""Decorator to see if anything has changed in the frame with land lot units.

	Args:
		func: The function to be decorated.

	Returns:
		The wrapper with the decorated function.

	"""
	@wraps(func)
	def wrapper(*args: Any, **kwargs: Any) -> Optional[Tuple[int, int, int, int]]:
		"""The wrapper of the decorator.
		
		Returns:
			The difference between screenshots before and after calling the funcion.
			If the difference is not found, None will be returned.

		"""
		dropdown_region = pg.locateOnScreen('assets/dropdowns.png', confidence=0.5)
		pg.click(*CENTER_POSITION)
		sleep(0.5)
		im_before = pg.screenshot(region=dropdown_region).convert('RGB')

		func(*args, **kwargs)

		pg.click(*CENTER_POSITION)
		sleep(0.5)
		im_after = pg.screenshot(region=dropdown_region).convert('RGB')

		difference = ImageChops.difference(im_before, im_after)
		return difference.getbbox() # type: ignore

	return wrapper
