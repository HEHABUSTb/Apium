import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.base.DriverClass import allure_step


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for loginpage
    _login_button = 'com.skill2lead.appiumdemo:id/Login'
    _enter_email = 'com.skill2lead.appiumdemo:id/Et4'
    _enter_password = 'com.skill2lead.appiumdemo:id/Et5'
    _click_login_button = 'com.skill2lead.appiumdemo:id/Btn3'
    _wrong_credentials = 'Wrong Credentials'
    _enter_admin_title = 'Enter Admin'
    _enter_admin_locator = 'text("Enter Admin")'
    _enter_admin_field = 'com.skill2lead.appiumdemo:id/Edt_admin'
    _enter_admin_click_button = 'com.skill2lead.appiumdemo:id/Btn_admin_sub'

    def click_login_button(self):
        self.allure_step('Click on login button in main menu')
        self.click_element(self._login_button)

    def enter_email(self, email = 'admin@gmail.com'):
        self.allure_step(f'Enter email {email}')
        self.send_text(email, self._enter_email)

    def enter_password(self, password='admin123'):
        self.allure_step(f'Enter password {password}')
        self.send_text(password, self._enter_password)

    def click_submit_login_button(self):
        self.allure_step('Submit email and password by click on login button')
        self.click_element(self._click_login_button)

    def verify_admin_screen(self):
        allure_step('Verify admin screen')
        title = self.get_element(self._enter_admin_locator, AppiumBy.ANDROID_UIAUTOMATOR)
        logging.info(f'Displayed title: {title.text}')
        assert self.is_displayed(self._enter_admin_locator, AppiumBy.ANDROID_UIAUTOMATOR), \
            f"Cant find a {self._enter_admin_title}"

    def enter_admin_text(self):
        text = 'Code2Lead'
        allure_step(f'Enter admin text: {text}')
        self.send_text(text, self._enter_admin_field)

    def click_enter_admin_button(self):
        allure_step(f'Click on enter admin submit')
        self.click_element(self._enter_admin_click_button)
