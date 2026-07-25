import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.by import By 
from time import sleep

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found", driver.page_source)

    def tearDown(self):
        self.driver.close()

prs = PythonOrgSearch()

prs.setUp()
prs.test_search_in_python_org()
prs.tearDown

if __name__ -- "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)