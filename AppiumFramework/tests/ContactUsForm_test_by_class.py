import logging
import unittest

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.base.DriverClass import Driver, allure_step
from appium.webdriver.common.appiumby import By, AppiumBy
from AppiumFramework.pages.ContactUsFormPage import ContactForm


@pytest.mark.All
@pytest.mark.usefixtures('driver')
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_object(self):
        self.contact_form = ContactForm(self.driver)

    def test_contact_form(self):
        allure_step('Contact form test')
        self.contact_form.click_contact_form()
        self.contact_form.verify_contact_page()

        self.contact_form.enter_name('Man')
        self.contact_form.enter_email('example@mail.com')
        self.contact_form.enter_address('street 93')
        self.contact_form.enter_mobile_number('+778782323')

        self.contact_form.click_submit_button()
        self.contact_form.screen_shot('Registration')
