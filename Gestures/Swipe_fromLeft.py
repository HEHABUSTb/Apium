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

driver.find_element(By.ID, 'com.code2lead.kwad:id/TabView').click()

print('Device Width and Height: ', driver.get_window_size())
# Store x and y in variables
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

# Right to Left
start_x_left = screenWidth * 0.9
end_x_left = screenWidth / 9
start_y_left = screenHeight / 2
end_y_left = screenHeight / 2

# LEft to right
start_x_right = screenWidth / 9
end_x_right = screenWidth * 0.8
start_y_right = screenHeight / 2
end_y_right = screenHeight / 2

actions = TouchAction(driver)
actions.long_press(None, start_x_left, start_y_left).move_to(None, end_x_left, end_y_left).release().perform()
time.sleep(2)
actions.long_press(None, start_x_right, start_y_right).move_to(None, end_x_right, end_y_right).release().perform()
