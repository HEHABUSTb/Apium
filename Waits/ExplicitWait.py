from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
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

"""
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=None)

button_enter_some_value = wait.until(lambda x: x.find_element(By.ID, 'com.code2lead.kwad:id/EnterValue'))
button_enter_some_value.click()

text_field = wait.until(lambda x: x.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys('Code2Lead'))
text_field.click()

driver.quit()
I prefer use implicitly wait 
"""

driver.implicitly_wait(5)

button_enter_some_value = driver.find_element(By.ID, 'com.code2lead.kwad:id/EnterValue')
button_enter_some_value.click()

# time.sleep(2)
text_field = driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys('Code2Lead')

driver.quit()