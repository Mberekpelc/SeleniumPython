import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
assert(driver.title == "The Internet")
element = driver.find_element(By.XPATH, "//*[@id='content']/div/p")
text = element.text
assert text == "Congratulations! You must have the proper credentials."
time.sleep(2)
