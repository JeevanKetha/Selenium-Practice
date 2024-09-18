from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create driver object
driver = webdriver.Edge()

# Navigate to a URL that delays loading (Replace sample URL with your URL )
driver.get("https://app.hubspot.com/login?hubs_signup-url=www.hubspot.com%2Fproducts%2Fcrm&hubs_signup-cta=nav-utility-login&hubs_content=www.hubspot.com%2Fproducts%2Fcrm&hubs_content-cta=nav-utility-login&uuid=3bf9a0dd-366e-413e-8ab5-784b92a2f266&_gl=1*er2zpp*_gcl_au*NDYzMDcxMy4xNzI1MzQ1OTY5*_ga*MTk4NDM2MjM4MC4xNzI1MzQ1OTY5*_ga_LXTM6CQ0XK*MTcyNTM0NTk2OS4xLjAuMTcyNTM0NTk2OS42MC4wLjA.")

try:
    # Fluent wait for the element to be present
    # ( Replace myDynamicElement elememnt with your elememnt id )
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
finally:
    # Quit the driver
    driver.quit()
