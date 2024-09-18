from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
driver =  webdriver.Edge(EdgeChromiumDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/profile/sign-in")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#main-container > div > div.css-1dbjc4n.r-13awgt0 > div > div.css-1dbjc4n.r-14lw9ot.r-qklmqi.r-1v0149v.r-1phboty.r-5kkj8d.r-nsbfu8 > div.css-1dbjc4n.r-18u37iz > div:nth-child(2) > div > div.css-1dbjc4n.r-1niwhzg.r-rs99b7.r-18u37iz").click()
time.sleep(5)
#guest=driver.find_element(By.CSS_SELECTOR,'#main-container > div > div.css-1dbjc4n.r-16y2uox > div > div > div > div > div.css-1dbjc4n.r-6ilu34.r-13yce4e.r-11kvaaj > div > div:nth-child(6)')
user_name=driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div[1]/div/div[2]/div[4]/div/div[2]/div')
password=driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div[1]/div/div[2]/div[5]/div/div[2]/div[1]/input')
login_btn=driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div[1]/div/div[2]/div[7]')
act_chains=ActionChains(driver)
act_chains.send_keys(user_name,'Jeevan')
act_chains.send_keys(password,'Qwerty')
act_chains.click(login_btn).perform()