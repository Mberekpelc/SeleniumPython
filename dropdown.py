#how to test dropdown elements on a web page
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# Initialize the Chrome driver
service = Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)      
driver.get("https://commitquality.com/practice-general-components") 
driver.maximize_window()
# Wait for the dropdown to be present
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])
dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dropdowns']//select")))
# Check if the dropdown is displayed
print("Display status:", dropdown.is_displayed())
print("Selected status:", dropdown.is_selected())
# Select an option from the dropdown
select = Select(dropdown)
select.select_by_visible_text("Option 3")
#select.select_by_value("1")
#select.select_by_index(1)

print("Selected status after selecting:", select.first_selected_option.text)
# Get all options from the dropdown
options = select.options
print("Total number of options:", len(options))
for option in options:
    print("Option:", option.text)
    if option.text == "Option 1":
        option.click()
        print("Selected status after clicking:", option.is_selected())
        break
# Close the browser
driver.quit()
