import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.by import By 
import time

elem_found = []

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        time.sleep(1)
        self.assertIn("Python", driver.title)
        time.sleep(1)
        elem = driver.find_element(By.NAME, "q")
        time.sleep(1)
        elem.send_keys("pycon")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertNotIn("No results found", driver.page_source)

    def tearDown(self):
        self.driver.close()

prs = PythonOrgSearch()

prs.setUp()
prs.test_search_in_python_org()
prs.tearDown

if __name__ -- "__main__":
    unittest.main()