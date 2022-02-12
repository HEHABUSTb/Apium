import unittest
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.base.DriverClass import Driver, allure_step
from appium.webdriver.common.appiumby import By, AppiumBy
from AppiumFramework.pages.LoginPage import LoginPage


@pytest.mark.All
@pytest.mark.usefixtures('driver')
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_object(self):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_login_page(self):
        self.login_page.key_code_action(4)
        self.login_page.allure_step('Login page test')
        self.login_page.click_login_button()
        self.login_page.enter_email()
        self.login_page.enter_password()
        self.login_page.click_submit_login_button()
        self.login_page.verify_admin_screen()
        self.login_page.enter_admin_text()
        self.login_page.click_enter_admin_button()

    @pytest.mark.run(order=1)
    def test_negative_login_page(self):
        self.login_page.allure_step('Negative login page test')
        self.login_page.click_login_button()
        self.login_page.enter_email('admin')
        self.login_page.enter_password('123')
        self.login_page.click_submit_login_button()
        self.login_page.verify_admin_screen()
