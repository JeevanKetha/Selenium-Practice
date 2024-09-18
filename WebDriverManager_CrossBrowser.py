from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
browserName = "edge"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print('please pass the correct browser name:'+ browserName)
    raise Exception('driver is not found')

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login?hubs_signup-url=www.hubspot.com%2Fproducts%2Fcrm&hubs_signup-cta=nav-utility-login&hubs_content=www.hubspot.com%2Fproducts%2Fcrm&hubs_content-cta=nav-utility-login&uuid=3bf9a0dd-366e-413e-8ab5-784b92a2f266&_gl=1*er2zpp*_gcl_au*NDYzMDcxMy4xNzI1MzQ1OTY5*_ga*MTk4NDM2MjM4MC4xNzI1MzQ1OTY5*_ga_LXTM6CQ0XK*MTcyNTM0NTk2OS4xLjAuMTcyNTM0NTk2OS42MC4wLjA.")
driver.find_element(By.ID, 'username').send_keys("Jeevan")
driver.find_element(By.ID, 'password').send_keys("Jeevan^1567")
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)

time.sleep(5)
driver.quit()

