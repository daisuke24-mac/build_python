import time
from selenium import webdriver

options = webdriver.ChromeOptions()
driver_path = 'C:/Users/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path, chrome_options = options)

driver.get('https://www.amazon.co.jp/')

mailad = driver.find_element_by_id("nav-link-accountList")
mailad.click()

login_id = driver.find_element_by_id("ap_email")
login_id.send_keys('')

nextb = driver.find_element_by_class_name("a-button-input")
nextb.click()
time.sleep(1)

password = driver.find_element_by_name("password")
password.send_keys('example')

nextb = driver.find_element_by_id("signInSubmit")
nextb.click()
time.sleep(1)
