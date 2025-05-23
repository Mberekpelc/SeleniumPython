from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
# Initialize the Chrome driver
service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")  
driver.maximize_window()
# Wait for the alert to be present
wait = WebDriverWait(driver, 10)
# Click the button to trigger the alert
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
button.click()
     # Switch to the alert
#alert = wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
# Print the alert text
print("Alert text is:", alert.text)
time.sleep(3)
# Accept the alert
alert.accept()
# Wait for the result text to be present
result = wait.until(EC.presence_of_element_located((By.ID, "result")))
# Print the result text
print("Result text:", result.text)

# Click the button to trigger the confirm alert
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']")))
button.click()
# Switch to the confirm alert
alert = wait.until(EC.alert_is_present())
# Print the confirm alert text
print("Confirm alert text:", alert.text)
# Dismiss the confirm alert
time.sleep(3)
alert.dismiss()
# Wait for the result text to be present
result = wait.until(EC.presence_of_element_located((By.ID, "result")))
# Print the result text
print("Result text after dismissing confirm alert:", result.text)


# Click the button to trigger the prompt alert
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Prompt']")))
button.click()
# Switch to the prompt alert
alert = wait.until(EC.alert_is_present())
# Print the prompt alert text 
print("Prompt alert text:", alert.text)
# Send text to the prompt alert
alert.send_keys("Hello, World!")
time.sleep(3)
# Accept the prompt alert
alert.accept()
# Wait for the result text to be present
result = wait.until(EC.presence_of_element_located((By.ID, "result")))
# Print the result text
print("Result text after accepting prompt alert:", result.text)
# Close the browser             
driver.quit()
