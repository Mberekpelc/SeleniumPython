import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
assert 'OrangeHRM' in driver.title
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
usernameInput = driver.find_element(By.NAME, "username")
usernameInput.send_keys("Admin")
passwordInput = driver.find_element(By.NAME, "password")
passwordInput.send_keys("admin123")
submitButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submitButton.click()
assert 'OrangeHRM' in driver.title
page_item= driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-list-check orangehrm-dashboard-widget-icon']")
print("Display status:", page_item.is_displayed())
time.sleep(5)

driver.close()
