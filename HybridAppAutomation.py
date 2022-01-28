from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3aXL_2'
#desired_caps['app'] = 'C:\\Users\\a_lyubinskiy\\Downloads\\Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
desired_caps["automationName"] = "UiAutomator2"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# Open url in browser
checkbox_chrome = driver.find_element(By.ID, 'com.android.chrome:id/send_report_checkbox')
checkbox_chrome.click()

button_accept = driver.find_element(By.ID, 'com.android.chrome:id/terms_accept')
button_accept.click()

button_negative = driver.find_element(By.ID, 'com.android.chrome:id/negative_button')
button_negative.click()

search_box_text = driver.find_element(By.ID, 'com.android.chrome:id/search_box_text')
search_box_text.click()

url_bar = driver.find_element(By.ID, 'com.android.chrome:id/url_bar')
url_bar.click()
url_bar.send_keys('http://www.dummypoint.com/seleniumtemplate.html')

driver.press_keycode(66)

# Get list of Contexts in App
appContexts = driver.contexts
print(appContexts)

# Switch to WebView
for appType in appContexts:
    if appType in ['WEBVIEW_chrome']:
        print('Switch to WebView')
        driver.switch_to.context(appType)

# Do some action in WebView
print('Try to find element user input')
user_input = driver.find_element(By.CSS_SELECTOR, '#user_input')
user_input.click()
user_input.send_keys('Code2Lead')

# Switch to Native app
for appType in appContexts:
    if appType in ['NATIVE_APP']:
        print('Switch to NATIVE_APP')
        driver.switch_to.context(appType)

url_bar.click()
url_bar.send_keys('http://www.kennisworld.com/')
driver.press_keycode(66)

time.sleep(7)
driver.quit()
