#EXAMPLE 1: Login into Facebook

from selenium import webdriver        #From selenium module import webdriver
from selenium.webdriver.common.keys import Keys   # From selenium module import Keys

user_name = "YOUR EMAILID"             #User is a variable which will be we used to store values of username.
password = "YOUR PASSWORD"             #Variable "password" will be used to store values of the password.
#driver = webdriver.Edge()
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()