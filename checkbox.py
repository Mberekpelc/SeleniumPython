import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# Wait for the checkbox to be present
wait = WebDriverWait(driver, 10)
checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='monday']")))
# Check if the checkbox is displayed
print("Display status:", checkbox.is_displayed())
# Check if the checkbox is enabled
print("Enabled status:", checkbox.is_enabled())
# Check if the checkbox is selected
print("Selected status:", checkbox.is_selected())
# Click the checkbox        
checkbox.click()
# Check if the checkbox is selected after clicking
print("Selected status after clicking:", checkbox.is_selected())
# Close the browser
driver.quit()
# The code above demonstrates how to interact with a checkbox using Selenium WebDriver in Python.

# Selecting for than one checkbox

service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# Wait for the checkboxes to be present
wait = WebDriverWait(driver, 10)
checkbox1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")))
print(len(checkbox1))
# Check if the checkboxes are displayed

for checkbox in checkbox1:
    print("Selected status:", checkbox.is_selected())
    # Click the checkboxes
    checkbox.click()
    # Check if the checkboxes are selected after clicking
    print("Selected status after clicking:", checkbox.is_selected())
# Close the browser
driver.quit()

# Selecting for than one checkbox by choice
service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# Wait for the checkboxes to be present
wait = WebDriverWait(driver, 10)
checkbox1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")))
# Check if the checkboxes are displayed
for checkbox in checkbox1:
    print("Selected status:", checkbox.is_selected())
    # Click the checkboxes
    if checkbox.get_attribute("value") == "monday"  or checkbox.get_attribute("id") == "tuesday":
        checkbox.click()
        # Check if the checkboxes are selected after clicking
        print("Selected status after clicking:", checkbox.is_selected())
time.sleep(5)
# Close the browser
driver.quit()
