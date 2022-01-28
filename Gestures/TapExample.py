from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel3aXL'
desired_caps['app'] = 'C:\\Users\\a_lyubinskiy\\Downloads\\Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps["automationName"] = "UiAutomator2"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# Scroll to long click button
button_long_click = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                    'UiScrollable(UiSelector()).scrollIntoView(resourceId("com.code2lead.kwad:id/LongClick"))')

action = TouchAction(driver)
action.tap(None, 531, 1360, 1)

action.perform()