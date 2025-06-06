from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service())
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
tRow = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
tColumn = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))

print(f"Number of row is: {tRow}")
print(f" Number of columns is: {tColumn}")

bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
print(bookName)

for r in range(2, tRow+1):
    row_data = []
    for c in range(1, tColumn+1):
        data = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[{c}]" ).text
        row_data.append(data)
 
    print(f"{row_data}", end="\n")

for r in range(2, tRow+1):
    authorName = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[1]").text
        bookPrice = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[4]").text
        print(f"{bookName}, {authorName}, {bookPrice}")

driver.quit()