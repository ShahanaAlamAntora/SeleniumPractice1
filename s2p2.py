#EXAMPLE 2: Login into Gmail & Check Title

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Chrome
#browser = webdriver.Chrome()
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
# Step 2) Navigate to Gmail
browser.get("http://www.gmail.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("YOUR EMAILID")
password.send_keys("YOUR PASSWORD")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Gmail"