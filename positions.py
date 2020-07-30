import pyautogui as pg

"""
Stores positions of all administrative units in TurboEWID.
"""

PRIMARY_UNIT_POSITION = (1887, 97)
SECONDARY_UNIT_POSITION = (1887, 126)
TERTIARY_UNIT_POSITION = (1887, 150)

DROPDOWNS_REGION = pg.locateOnScreen('assets/dropdowns.png', confidence=0.5)
