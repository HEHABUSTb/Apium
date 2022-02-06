import allure
from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
import time


class Driver:

    def getDriverMethod(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel_3a_XL'
        desired_caps['app'] = 'C:\\Users\\Alex\\Downloads\\Android_Appium_Demo.apk'
        desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
        desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'
        desired_caps["automationName"] = "UiAutomator2"
        # new desired_caps for parallel working
        # desired_caps['udid'] = device_uiid
        # desired_caps['systemPort'] = systemPort  # Default is 8200 an in range 8200 - 8299

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        return driver


def allure_step(text: str):
    with allure.step(text):
        pass
