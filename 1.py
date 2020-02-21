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
        driver.get("https://admin:admin123@staging.shopia.com")
        time.sleep(10)
        driver.find_element_by_xpath("//form[@data-product-sku='2034866R']/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[@class='action showcart']").click()
        driver.find_element_by_xpath("//button[@id='top-cart-btn-checkout']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@data-role='proceed-to-checkout']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[@class='continue-guest']").click()
        time.sleep(15)
        driver.find_element_by_xpath("//input[@name='lastname']").send_keys(
                                       'test'+str(random.randrange(100)), Keys.ENTER)
        driver.find_element_by_xpath("//input[@name='firstname']").send_keys(
                                       '1test'+str(random.randrange(100)), Keys.ENTER)

        elem = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
        elem.send_keys('test'+str(random.randrange(10000))+'@gmail.com', Keys.ENTER)
        # elem = driver.find_elements_by_xpath("//input[@name='username']")[1]
        # ActionChains(driver).move_to_element(elem).send_keys('test'+str(random.randrange(10000))+'@gmail.com', Keys.ENTER).perform()

        # driver.find_elements_by_xpath("//input[@name='username']")[1].send_keys(
        #                                'test'+str(random.randrange(10000))+'@gmail.com', Keys.ENTER)
        time.sleep(1)
        # driver.find_elements_by_xpath("//input[@name='telephone']")[1].send_keys(
        #                                  random.randint(1000000, 9999999), Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@name='street[1]']")[1].send_keys(
                                         '1test'+str(random.randrange(100)), Keys.ENTER)
        time.sleep(1)
        # driver.find_elements_by_xpath("//input[@placehodler='Line2']")[1].send_keys(
        #                                 '1test'+str(random.randrange(100)), Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@name='region']")[1].send_keys(
                                        '1test'+str(random.randrange(100)), Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@name='sity']")[1].send_keys(
                                       '1test'+str(random.randrange(100)), Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@name='postcode']")[1].send_keys(
                                       random.randrange(1000, 9999), Keys.ENTER)

        time.sleep(19)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
