from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Path to your chromedriver
s = Service("E:/apps/Downloads/chromedriver-win64/chromedriver.exe")

# Start Chrome browser
driver = webdriver.Chrome(service=s)

# Open Google
driver.get("https://www.google.com")

#find the search input box by using Xpath
user_input = driver.find_element(by = By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys("CampusX")
time.sleep(2)
user_input.send_keys(Keys.ENTER)

# link = driver.find_element(by = By.XPATH, value='*[@id="ixcYae"]/div/div/div/div/div/div/div[1]/div/span/a')
# link.click()
# time.sleep(2)
link = driver.find_element(by = By.XPATH, value='//*[@id="ixcYae"]/div/div/div/div/div/div/div[1]/div/span/a/div/div/div/div[2]/cite')
link.click()
time.sleep(2)

# link2 = driver.find_element(by = By.XPATH, value='//*[@id="menu-item-107"]/a')

# Wait for user input to close the browser
input("Press Enter to close the browser...")

# Close the browser manually after user input
driver.quit()
