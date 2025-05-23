from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import requests

# Initialize the Chrome driver  
service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
link.click()

# Wait for the registration form to be visible
login_form = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Log in']")))

# Assert the registration form is displayed
assert login_form.is_displayed(), "Registration form is not displayed"

driver.quit()

# How to test broken links

service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
all_links = driver.find_elements(By.TAG_NAME, "a")
print("Total number of links: ", len(all_links))
for link in all_links:
    url = link.get_attribute("href")
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code >= 400:
        print("Link is broken: ", url)
    else:
        print("Link is working: ", url)
# Close the browser
driver.quit()
# The code above demonstrates how to test for broken links using Selenium WebDriver in Python.
