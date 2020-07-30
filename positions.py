import pyautogui as pg
from typing import Final

"""
Stores positions of all administrative units in TurboEWID.
"""

PRIMARY_UNIT_POSITION: Final = (1887, 97)
SECONDARY_UNIT_POSITION: Final = (1887, 126)
TERTIARY_UNIT_POSITION: Final = (1887, 150)

DROPDOWNS_REGION: Final = pg.locateOnScreen('assets/dropdowns.png', confidence=0.5)

CENTER_POSITION = (1000, 500)
