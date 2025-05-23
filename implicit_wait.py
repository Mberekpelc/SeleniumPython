from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://google.co.uk/")
driver.maximize_window
driver.implicitly_wait(10)
driver.find_element(By.ID, "L2AGLb").click()
searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("Selenium")
searchbox.submit()

print("Page title is: ", driver.title)

driver.find_element(By.XPATH, "//h3[text()='Selenium')]").click()
driver.quit()


