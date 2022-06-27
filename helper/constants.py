import os

BROWSER_NAME = 'chrome'
DRIVER_IMPLICIT_WAIT = 10
DRIVER_EXPLICIT_WAIT = 35
TEMP_DIR = ''

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_FILENAME = PROJECT_DIR + os.path.normpath("/latest.log")
CONFIG_FILENAME = PROJECT_DIR + os.path.normpath("/config/config.json")

TEMP_SCREENSHOT_DIR = ''
