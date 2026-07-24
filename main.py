from selenium import webdriver 
# Provides all the webdriver implementations such as:
# Firefox, Chrome, IE (Internet Explorer), Remote
from selenium.webdriver.common.keys import Keys # Provides keys found in keyboard  
from selenium.webdriver.common.by import By # Provides classes to locate elements 
                                            # within a document

# Create instance of Chrome Webdriver
driver = webdriver.Chrome()
# 
driver.get("http://www.python.org")

assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()