from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3aXL'
desired_caps['app'] = 'C:\\Users\\Alex\\Downloads\\Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps["automationName"] = "UiAutomator2"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#element_by_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENTER SOME VALUE")')
element_by_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("ENTER SOME VALUE")')
element_by_text.click()
