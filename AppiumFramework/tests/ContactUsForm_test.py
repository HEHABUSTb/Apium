import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.base.DriverClass import Driver, allure_step
from appium.webdriver.common.appiumby import By, AppiumBy


@pytest.mark.All
def test_allure_report():
    allure_step('Check')
    logging.info('Launch App')
    driver = Driver().getDriverMethod()

    base_page = BasePage(driver)
    base_page.explicitly_wait('com.skill2lead.appiumdemo:id/ContactUs')

    # button_contact_us = base_page.get_element('com.skill2lead.appiumdemo:id/ContactUs').click()

    base_page.click_element('com.skill2lead.appiumdemo:id/ContactUs')
    base_page.is_displayed('com.skill2lead.appiumdemo:id/Et2')
    base_page.send_text('Name', 'text("Enter Name")', AppiumBy.ANDROID_UIAUTOMATOR)
    base_page.screen_shot('Contact_us_form')


