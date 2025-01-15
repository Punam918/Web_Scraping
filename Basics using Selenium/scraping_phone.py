from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver
s = Service("C:/Users/admin/Desktop/chromedriver-win64/chromedriver.exe")

# Start Chrome browser
driver = webdriver.Chrome(service=s)
#loading the website
driver.get("https://www.smartprix.com/mobiles/")
time.sleep(2)

driver.find_element(by = By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)
driver.find_element(by = By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()

time.sleep(2)

driver.find_element(by = By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
time.sleep(2)
driver.find_element(by = By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
time.sleep(2)



old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.find_element(by = By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == old_height:
        break
    old_height = new_height
    
    
html = driver.page_source
with open('smart.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Wait for user input to close the browser
input("Press Enter to close the browser...")

# Close the browser manually after user input
driver.quit()
