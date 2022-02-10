import logging
import time
from appium.webdriver.common.appiumby import By, AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_value, locator_type=By.ID):
        try:
            logging.info(f'Try to click on element by {locator_type} and {locator_value}')
            element = self.driver.find_element(locator_type, locator_value)
            element.click()

        except Exception as e:
            logging.info(f"Can't clicked by {locator_type} and {locator_value} raise {e}")
            raise e

    def explicitly_wait(self, locator_value: str, locator_type=By.ID, timeout=10):
        logging.info(f'Start to Explicitly wait element by {locator_type}, {locator_value} with timeout {timeout}')
        start_time = time.perf_counter()

        wait = WebDriverWait(self.driver, timeout, poll_frequency=2, ignored_exceptions=None)
        element = wait.until(lambda x: x.find_element(locator_type, locator_value))

        elapsed_time = time.perf_counter() - start_time
        elapsed_time = round(elapsed_time, 3)
        logging.info(f'Element "{locator_value}" is appearing in {elapsed_time} seconds')

        return element

    def get_element(self, locator_value, locator_type=By.ID):
        try:
            logging.info(f"Try to find element by {locator_type} and {locator_value}")
            element = self.driver.find_element(locator_type, locator_value)

            return element
        except Exception as e:
            logging.info(f"Can't find element by {locator_type} and {locator_value} raise {e}")
            raise e

    def is_displayed(self, locator_value, locator_type=By.ID):
        element = self.driver.find_element(locator_type, locator_value)
        if element.is_displayed() is True:
            logging.info(f'Element "{locator_value}" is displayed')
            return True
        else:
            logging.info(f"Element with {locator_type} and {locator_value} is not displayed")
            return False

    def screen_shot(self, screenshot_name='Screenshot'):
        file_name = screenshot_name + "_" + time.strftime("%H_%M_%S") + ".png"
        screenshot_path = 'profile\\' + file_name

        try:
            logging.info(f'Try to save screenshot in {screenshot_path}')
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            # I don't know why but statement doesn't work properly
            logging.info(f"Can't take a screenshot raise in {screenshot_path}")
            raise e

    def send_text(self, text, locator_value, locator_type=By.ID):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            element.send_keys(text)
            logging.info(f'Send "{text}" to {locator_value} was successful')

        except Exception as e:
            logging.info(f"Can't send text by {locator_type} and {locator_value} raise {e}")
            raise e
