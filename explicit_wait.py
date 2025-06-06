from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=webdriver.chrome.service.Service())
#Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
#driver = webdriver.Chrome(service=Service_obj)
from selenium.webdriver import ActionChains

myWait = WebDriverWait(driver, timeout= 10, poll_frequency=2, ignored_exceptions=[Exception])
driver.get("https://google.co.uk/")
driver.maximize_window

driver.find_element(By.ID, "L2AGLb").click()
searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("Selenium")
searchbox.submit()

searchbox= myWait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
print("Page title is: ", driver.title)

searchbox.click()
driver.quit()
