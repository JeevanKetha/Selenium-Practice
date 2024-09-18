from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# ... (rest of your imports)

class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        self.option_list = driver.find_elements(By.CSS_SELECTOR, '#Alh6id > div.erkvQe/ul/li')

    def search(self, query):
        self.search_box.send_keys(query)
        self.search_box.submit()

    def get_search_suggestions(self):
        return self.option_list

# ... (rest of your code)

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
search_page = GoogleSearchPage(driver)

driver.get("https://www.google.co.in/")
search_page.search("shraddha kapoor")

wait = WebDriverWait(driver, 10)
for ele in search_page.get_search_suggestions():
    wait.until(expected_conditions.element_to_be_clickable(ele))
    print(ele.text)
    if ele.text == "shraddha kapoor relationships":
        ele.click()
        break