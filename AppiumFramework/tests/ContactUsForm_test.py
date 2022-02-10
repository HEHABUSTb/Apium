import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.base.DriverClass import Driver, allure_step
from appium.webdriver.common.appiumby import By, AppiumBy
from AppiumFramework.pages.ContactUsFormPage import ContactForm


@pytest.mark.All
def test_allure_report():
    allure_step('Contact form test')
    logging.info('Launch App')
    driver = Driver().getDriverMethod()

    contact_form = ContactForm(driver)
    contact_form.click_contact_form()
    contact_form.verify_contact_page()

    contact_form.enter_name('Man')
    contact_form.enter_email('example@mail.com')
    contact_form.enter_address('street 93')
    contact_form.enter_mobile_number('+778782323')

    contact_form.click_submit_button()
    contact_form.screen_shot('Registration')



