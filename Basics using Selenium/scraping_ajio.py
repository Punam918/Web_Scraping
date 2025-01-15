from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver
s = Service("C:/Users/admin/Desktop/chromedriver-win64/chromedriver.exe")

# Start Chrome browser
driver = webdriver.Chrome(service=s)

# Open Google
driver.get("https://www.ajio.com/men-backpacks/c/830201001")

old_height = driver.execute_script('return document.body.scrollHeight')
print(old_height)
# driver.execute_script('window.scrollTo(0,innerHeight )')

counter = 1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(counter)
    counter += 1
    print(old_height)
    print(new_height)
    
    if new_height == old_height:
        break
    

    old_height = new_height
    
    
#copy the contents of the whole web page from top to bottom in html format
html = driver.page_source
with open('ajio.html', 'w', encoding='utf-8') as f:
    f.write(html)
# Wait for user input to close the browser
input("Press Enter to close the browser...")

# Close the browser manually after user input
driver.quit()
