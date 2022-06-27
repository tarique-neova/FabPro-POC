import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helper import constants


def wait_for_element_to_be_present_using_xpath(driver, xpath):
    try:
        element = WebDriverWait(driver, constants.DRIVER_EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        return element.is_displayed()
    except Exception as ex:
        logging.error("Caught Exception while waiting for element present: {}".format(ex))
        return False


def get_element_text(driver, locators, attribute=""):
    logging.info("Getting element text: locators = {}, attribute = {}".format(locators, attribute))
    try:
        if attribute.__eq__(""):
            return str(driver.find_element_by_xpath(locators).text)
        return str(driver.find_element_by_xpath(locators).get_attribute(attribute))
    except Exception as ex:
        logging.error("Unable to fetch text of element {}".format(ex))
        return None


def get_element(driver, locators):
    try:
        wait_for_element_to_be_present_using_xpath(driver, locators)
        return driver.find_element_by_xpath(locators)
    except Exception as ex:
        logging.error("Unable to find element {}".format(ex))
        return None


def wait_for_the_element_to_be_clickable_using_xpath(driver, xpath):
    try:
        WebDriverWait(driver, constants.DRIVER_EXPLICIT_WAIT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return True
    except Exception as ex:
        logging.error("Exception occurred while waiting for clickable element -> {} ".format(ex))
        return False


def wait_for_element_visibility_using_xpath(driver, xpath):
    try:
        WebDriverWait(driver, constants.DRIVER_EXPLICIT_WAIT).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return True
    except Exception as ex:
        logging.error("Exception occurred while waiting for element visibility: {} ".format(ex))
        return False


def accept_alert(driver):
    try:
        driver.switch_to_alert().accept()
    except:
        pass


def cancel_alert(driver):
    try:
        driver.switch_to_alert().dismiss()
    except:
        pass


def javascript_click(driver, element):
    try:
        driver.execute_script("arguments[0].click();", element)
        return True
    except:
        return False


def switch_browser_tab(driver):
    try:
        previous_window = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        time.sleep(2)
        return driver, previous_window
    except Exception as ex:
        logging.error("Error while switching browser tab, Exception occurred -> {}".format(ex))
        return None, None


def switch_to_default(driver, previous_window):
    try:
        driver.switch_to_window(previous_window)
        return driver
    except:
        return None


def click_element_by_locator(driver, locator):
    try:
        btn = driver.find_element_by_xpath(locator)
        btn.click()
    except Exception as ex:
        logging.error("Exception : click_element_by_locator - {}".format(ex))
        return False


def click_to_element(driver, xpath):
    try:
        WebElement = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        actions.click(WebElement).perform()
        logging.info("Clicked to element by ActionChains method")
        driver.implicitly_wait(constants.DRIVER_IMPLICIT_WAIT)
        return True
    except Exception as ex:
        driver.implicitly_wait(constants.DRIVER_IMPLICIT_WAIT)
        logging.error("Exception occurred while click to element by ActionChains method:  {} ".format(ex))
        return False


def move_to_element_and_click_by_locator(driver, webelement, locator):
    try:
        btn = webelement.find_element_by_xpath(locator)
        driver.implicitly_wait(0)
        actions = ActionChains(driver)
        actions.move_to_element(btn)
        actions.click(btn)
        actions.perform()
        driver.implicitly_wait(constants.DRIVER_IMPLICIT_WAIT)
        return True
    except:
        driver.implicitly_wait(constants.DRIVER_IMPLICIT_WAIT)
        return False


def scroll_to_particular_element(driver, element):
    """
     :Args:
         - element:  the WebElement to move to
    """
    try:
        driver.implicitly_wait(0)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        driver.implicitly_wait(constants.DRIVER_IMPLICIT_WAIT)
        return True
    except Exception as ex:
        driver.implicitly_wait(constants.DRIVER_IMPLICIT_WAIT)
        logging.error("Got error while scrolling, Exception occurred => {}".format(ex))
        return False


def capture_screenshot(driver, file_name):
    try:
        # driver.get_screenshot_as_file(constants.TEMP_SCREENSHOT_DIR + "/" + file_name + ".png")
        driver.save_screenshot(constants.TEMP_SCREENSHOT_DIR + "/" + file_name + ".png")
    except Exception as ex:
        logging.error("Unable to Store Screenshot - Expection => " + str(ex))
        pass
