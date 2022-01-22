from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3aXL'
desired_caps['app'] = 'C:\\Users\\Alex\\Downloads\\Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps["automationName"] = "UiAutomator2"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#element_by_xpath = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Btn1"]')
element_by_xpath = driver.find_element(By.XPATH, '//android.widget.Button[1]')
element_by_xpath.click()
time.sleep(2)

text_field = driver.find_element(By.XPATH, '//android.widget.EditText').send_keys('Code2Lead')
time.sleep(2)
driver.quit()
