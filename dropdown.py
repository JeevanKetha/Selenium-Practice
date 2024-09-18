from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select

import time

def select_values(optionslist,value):
    if not value[0]=="all":
        for ele in drop_list:
            print(ele.text)
            for k in range (len(value)):
                if ele.text==value[k]:
                    ele.click()
                    break

    else:
        try:
            for ele in optionslist:
                ele.click()
        except Exception as e:
            print(e)
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,'justAnInputBox').click()

time.sleep(5)

drop_list = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')

#values_list = ['choice 2', 'choice 3']
values_list = ['choice 2']
#values_list = ['all']
select_values(drop_list, 'values_list')
#select_values(drop_list, 'values_list')
#select_values(drop_list, 'values_list')

for ele in drop_list:
    print(ele.text)
    if ele.text == 'choice 2':
        ele.click()
        break

