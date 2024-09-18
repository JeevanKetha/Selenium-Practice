from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
import time

driver =  webdriver.Edge(EdgeChromiumDriverManager().install())

#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.co.in/")
#print(driver.title)
driver.implicitly_wait(5)

driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("selenium with python")
option_list = driver.find_elements(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9.EyBRub')

print(len(option_list))

#wait = WebDriverWait(driver, 10)
for ele in option_list:
    print(ele.text)







