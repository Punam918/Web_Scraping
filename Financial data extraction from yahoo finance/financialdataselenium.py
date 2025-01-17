from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your chromedriver
s = Service("E:/apps/Downloads/chromedriver-win64/chromedriver.exe")

# Start Chrome browser
driver = webdriver.Chrome(service=s)



#top gainers first page
# Load the website
data1 = driver.get("https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=100")

html = driver.page_source
with open('financialdatatopgainers.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
time.sleep(2)




#top gainers second page
data2 = driver.get("https://finance.yahoo.com/markets/stocks/gainers/?start=100&count=100")

html = driver.page_source
with open('financialdatatopgainers2.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
time.sleep(2)



#top loosers

data3 = driver.get("https://finance.yahoo.com/markets/stocks/losers/?start=0&count=100")

html = driver.page_source
with open('financialdatatoploosers.html', 'w', encoding='utf-8') as f:
    f.write(html)


#Trendingdata

data4 = driver.get("https://finance.yahoo.com/markets/stocks/trending/")

html = driver.page_source
with open('trending.html', 'w', encoding='utf-8') as f:
    f.write(html)



# Keep the browser open for user interaction
input("Press Enter to close the browser...")

# Close the browser
driver.quit()

