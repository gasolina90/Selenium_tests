from selenium import webdriver 
# Provides all the webdriver implementations such as:
# Firefox, Chrome, IE (Internet Explorer), Remote
from selenium.webdriver.common.keys import Keys # Provides keys found in keyboard  
from selenium.webdriver.common.by import By # Provides classes to locate elements 
                                            # within a document
import time

# Create instance of Chrome Webdriver
driver = webdriver.Chrome()
# Webdriver will automatically wait until the page has fully loaded
driver.get("http://www.python.org")

# Python test
assert "Python" in driver.title
# Find singular HTML elements by attribute
elem = driver.find_element(By.NAME, "q")
# Send keys. Be safe and clear the input field
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Python test
assert "No results found." not in driver.page_source
# Sleepy time to see what the heck happened
time.sleep(5)
driver.close()