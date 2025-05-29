import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
assert driver.title == "OrangeHRM"
wait = WebDriverWait(driver, 10, poll_frequency= 2, ignored_exceptions=[Exception])
currentWindowID = driver.current_window_handle
print(currentWindowID)
newPage = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "OrangeHRM, Inc")))
newPage.click()

windowIDs = driver.window_handles
parentWindow = windowIDs[0]
childWindow = windowIDs[1]
driver.switch_to.window(childWindow)
print(f"title of the child window is: {driver.title}")
driver.switch_to.window(parentWindow)
print(f"title of the parent window is: {driver.title}")

for windID in windowIDs:
    driver.switch_to.window(windID)
    print(driver.title)
    if driver.title == "OrangeHRM":
        driver.close()

time.sleep(5)
driver.quit()