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

buttons = driver.find_elements(By.CLASS_NAME, 'android.widget.Button')

for element in buttons:
    print(element.text)
    if 'ScrollView' in element.text:
        element.click()
        print('Clicked!')
        break

time.sleep(2)
driver.quit()
