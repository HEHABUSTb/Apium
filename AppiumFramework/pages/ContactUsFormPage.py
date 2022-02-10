import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.base.DriverClass import allure_step


class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ID Locators values for ContactUsForm
    _contact_form_button = 'com.skill2lead.appiumdemo:id/ContactUs'
    _page_title_locator = 'text("Contact Us form")'
    _page_title_text = "Contact Us form"
    _enter_name = 'com.skill2lead.appiumdemo:id/Et2'
    _enter_email = 'com.skill2lead.appiumdemo:id/Et3'
    _enter_address = 'com.skill2lead.appiumdemo:id/Et6'
    _enter_mobile_number = 'com.skill2lead.appiumdemo:id/Et7'
    _submit_button = 'com.skill2lead.appiumdemo:id/Btn2'

    def click_contact_form(self):
        allure_step('Click on Contact Form')
        self.click_element(self._contact_form_button)

    def click_submit_button(self):
        allure_step('Click on submit button')
        self.click_element(self._submit_button)

    def verify_contact_page(self):
        allure_step('Verify contact us form page')
        title = self.get_element('text("Contact Us form")', AppiumBy.ANDROID_UIAUTOMATOR)
        logging.info(f'Displayed title: {title.text}')
        assert self.is_displayed(f'text("Contact Us form")', AppiumBy.ANDROID_UIAUTOMATOR),\
            f"Cant find a {self._page_title_text}"

    def enter_name(self, text: str):
        allure_step('Enter the name')
        self.send_text(text, self._enter_name)

    def enter_email(self, text: str):
        allure_step('Enter email address')
        self.send_text(text, self._enter_email)

    def enter_address(self, text: str):
        allure_step('Enter address')
        self.send_text(text, self._enter_address)

    def enter_mobile_number(self, text: str):
        allure_step('Enter mobile phone')
        self.send_text(text, self._enter_mobile_number)

