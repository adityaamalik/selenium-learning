import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://adityamalik.com/")
print(driver.title)

elements = driver.find_elements(By.CLASS_NAME, 'link_design')

for e in elements:
    print(e.text)

time.sleep(5)

driver.quit()
