from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.eirhealth.com/")
        time.sleep(10)
        driver.find_element_by_xpath("//button[@class='action primary large-button']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)
        driver.find_element_by_xpath("//a[@title='Proceed to Checkout']").click()
        time.sleep(15)

        elem = driver.find_element_by_xpath("//input[@name='lastname']")
        logging.warning(elem)
        driver.find_element_by_xpath("//input[@name='lastname']").send_keys(
                                        'test'+str(random.randrange(100)), Keys.ENTER)
        driver.find_elements_by_xpath("//input[@name='firstname']")[1].send_keys(
                                        '1test'+str(random.randrange(100)), Keys.ENTER)
def tearDown(self):
     self.driver.close()

if __name__ == "__main__":
 unittest.main()
