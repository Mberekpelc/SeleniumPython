import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//button[@id='ez-accept-all']").click()

input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")
input1.send_keys("Welcome to Selenium")

act = ActionChains(driver)
act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
act.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()
print(input1.text)
time.sleep(3)
