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
time.sleep(2)
driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
assert "Automation Demo Site" in driver.page_source
assert (driver.title == "Frames")
print(driver.title)
popup_present = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]")

if popup_present:
    popup_present.click()

driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()
outerFrame= driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)
innerFrame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerFrame)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")
driver.switch_to.parent_frame()

time.sleep(2)
driver.quit()