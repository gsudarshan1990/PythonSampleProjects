from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(5)
element1=driver.find_element_by_id('nav-link-shopall')
actions=ActionChains(driver)
actions.move_to_element(element1).perform()
element2=driver.find_element_by_xpath('//div[@id="nav-flyout-shopAll"]/div[2]/span[3]/span[contains(text(),"Kindle E-Readers & eBooks")]')
actions.move_to_element(element2).perform()
element3=driver.find_element_by_xpath('//span[contains(text(),"Prime Reading")]')
element3.click()
print(driver.current_url)
time.sleep(5)
driver.quit()
