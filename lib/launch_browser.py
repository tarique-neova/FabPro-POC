import logging
import platform
import sys

from selenium import webdriver

from helper import constants


def launch_browser():
    try:
        browser_name = str(constants.BROWSER_NAME).lower()
        temp_folder = str(constants.TEMP_DIR)
        if browser_name.__eq__("chrome"):
            chrome_options = webdriver.ChromeOptions()
            preferences = {"download.default_directory": "" + temp_folder + ""}
            chrome_options.add_experimental_option("prefs", preferences)
            chrome_options.add_argument("enable-automation")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            if platform.system() == 'Linux':
                chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--dns-prefetch-disable")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(chrome_options=chrome_options)
        elif browser_name.__eq__("firefox"):
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", temp_folder)
            profile.set_preference("browser.helperApps.alwaysAsk.force", False)
            profile.set_preference("browser.helperApps.neverAsk.openFile",
                                   "image/png, text/html, image/tiff, text/csv, application/zip, application/octet-stream,application/json")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "image/png, text/html, image/tiff, text/csv, application/zip, application/octet-stream,application/json")
            driver = webdriver.Firefox(firefox_profile=profile, log_path=None)
        elif browser_name.__eq__("safari"):
            driver = webdriver.Safari()
        else:
            logging.error("The Browser Name To Be Launched Is Incorrect. Please Retry")
            sys.exit()
        driver.implicitly_wait(constants.DRIVER_IMPLICIT_WAIT)
        driver.maximize_window()
        return driver
    except:
        logging.error(
            "Exception Occurred In Launching Driver. Please Check If Respective 'drivers' are added to PATH Variable")
        sys.exit()
