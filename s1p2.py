#EXAMPLE 1: Login into Gmail

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.get("https://www.gmail.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()