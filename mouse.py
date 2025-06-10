import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains


# Perform mouse over action
Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
users = driver.find_element(By.LINK_TEXT, "Users")

act = ActionChains(driver)

act.move_to_element(users).click().perform()

time.sleep(3)
driver.quit()

## To perform right click action

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(5)

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
act = ActionChains(driver)

act.context_click(button).perform()

time.sleep(3)
driver.quit()

### How to perform double click action

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

inputBox = driver.find_element(By.XPATH, "//input[@id='field1']")
inputBox.clear()
inputBox.send_keys("Welcome 1")
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

act = ActionChains(driver)

act.double_click(button).perform()

time.sleep(3)
driver.quit()


## How to perform drag and drop

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

dragBox = driver.find_element(By.XPATH, "//*[@id='draggable']")
dropBox = driver.find_element(By.XPATH, "//*[@id='droppable']")

act = ActionChains(driver)
act.drag_and_drop(dragBox,dropBox).perform()

time.sleep(3)
driver.quit()


## Performing slider bar

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

minslider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
maxslider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print(minslider.location)
print(maxslider.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(minslider, 50, 0).perform()
act.drag_and_drop_by_offset(maxslider, -40, 0).perform()

time.sleep(3)
driver.quit()


## Perform scroll actions 

Service_obj =Service("/Users/Lawrence.Mberekpe/Workspace/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.implicitly_wait(5)

act = ActionChains(driver)
# act.scroll_by_amount(0,3000).perform()
# time.sleep(3)

## another way using javascript execution ####
driver.execute_script("window.scrollBy(0, 3000)", "") ## Scroll to a point specified
time.sleep(2)
flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Jordan']")
driver.execute_script("arguments[0].scrollIntoView();", flag) ## Scroll to a particular element
time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") ## Scroll to end of page
time.sleep(3)
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)") ## Scroll to beginning of page


time.sleep(3)
driver.quit()
