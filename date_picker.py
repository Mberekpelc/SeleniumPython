import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("06/20/2025")
time.sleep(2)

driver.quit()

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

year = "2026"
month = "May"
day = "25"

Month_and_year = month +" " + year

print(Month_and_year)

datePicker = driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon ==month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
        
# driver.find_element(By.LINK_TEXT, day).click() ### another way to get the date since it has an anchor tag
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in dates:
    if date.text == day:
        date.click()
        break
time.sleep(3)
driver.quit()

## Managing selection of date by dropdown

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
myWait = WebDriverWait(driver, 5)
dateInput = myWait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='dob']")))
dateInput.click()
monthPicker = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
monthPicker.select_by_visible_text("Dec")
yearPicker = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
yearPicker.select_by_visible_text("1990")

#driver.find_element(By.LINK_TEXT, "20").click()

allDates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")  
for date in allDates:
    if date.text == "25":
        date.click()
        break
    
time.sleep(6)
driver.quit()