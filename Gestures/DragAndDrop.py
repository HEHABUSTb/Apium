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

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                    'UiScrollable(UiSelector()).scrollIntoView(text("DRAGANDDROP"))').click()

image_kw = driver.find_element(By.ID, 'com.code2lead.kwad:id/ingvw')
area_for_drop = driver.find_element(By.ID, 'com.code2lead.kwad:id/layout2')

actions = TouchAction(driver)
actions.long_press(image_kw).move_to(area_for_drop).release().perform()

driver.quit()
