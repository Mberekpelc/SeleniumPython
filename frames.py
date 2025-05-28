# how to handle iframes 

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa-automation-practice.netlify.app/iframe")
#driver.get("https://commitquality.com/practice-iframe")
#driver.get("https://rori4.github.io/selenium-practice/#/pages/practice/iframe-form")
assert "Iframe Example" in driver.page_source

iframes = driver.find_elements(By.TAG_NAME, "iframe")

print(f"Number of iframes on the page: {len(iframes)}")

#driver.switch_to.frame(0)
driver.switch_to.frame("iframe-checkboxes")
driver.find_element(By.XPATH, "//a[@id='learn-more']").click()

time.sleep(5)
driver.quit()