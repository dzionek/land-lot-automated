from typing import Tuple, Callable, Any, Optional
from functools import wraps
from PIL import ImageChops
from time import sleep
import pyautogui as pg

from positions import DROPDOWNS_REGION, CENTER_POSITION

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
		sleep(1)
		pg.click(*CENTER_POSITION)
		im_before = pg.screenshot(region=DROPDOWNS_REGION).convert('RGB')

		func(*args, **kwargs)

		pg.click(*CENTER_POSITION)
		im_after = pg.screenshot(region=DROPDOWNS_REGION).convert('RGB')

		difference = ImageChops.difference(im_before, im_after)
		return difference.getbbox() # type: ignore

	return wrapper
