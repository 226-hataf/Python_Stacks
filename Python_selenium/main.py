from telnetlib import EC
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait

#PATH = "C:\drivers\chromedriver.exe"

#driver = webdriver.Chrome(PATH)

#driver.get("https://techwithtim.net")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://techwithtim.net")


print(driver.title)


search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "main")))
    if main:
        print(f"main:{main}")
        time.sleep(100)
    # print(main.text)

except:
    driver.quit()
    time.sleep(100)

