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
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath("//form[@data-product-sku='1309000038901']/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("//form[@data-product-sku='1309000038901']/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@class='fancybox-close']").click()
        time.sleep(5)
        # WARNING:
        # driver.get("https://staging.shopia.com/vitu-mars-11-16gb-rom-2gb-ram-dual-sim-dual-hd-camera-face-id-4g-lte-smartphone-dark-red.html")
        # time.sleep(10)
        # driver.find_element_by_xpath("//label[@for='economy_economy']").click()
        # time.sleep(10)
        # continue_link = driver.find_element_by_link_text('Shipping methods can')
        #
        # time.sleep(10)
        # assert "Shipping methods can be selected in cart page for multiple items" not in driver.page_source
        time.sleep(4)
        driver.find_element_by_xpath("//a[@class='action showcart']").click()
        driver.find_element_by_xpath("//button[@id='top-cart-btn-checkout']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//button[@data-role='proceed-to-checkout']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//a[@class='continue-guest']").click()
        time.sleep(10)
        driver.find_element_by_xpath("//input[@name='lastname']").send_keys(
                                       'test'+str(random.randrange(100)), Keys.ENTER)
        driver.find_element_by_xpath("//input[@name='firstname']").send_keys(
                                       '1test'+str(random.randrange(100)), Keys.ENTER)
        driver.find_elements_by_xpath("//input[@name='username']")[1].send_keys(
                                       'test'+str(random.randrange(10000))+'@gmail.com', Keys.ENTER)
        logging.warning(driver.find_elements_by_xpath("//input[@name='telephone']"))
        driver.find_element_by_xpath("//input[@name='telephone']").send_keys(' 77 '+
                                         str(random.randint(100000, 999999)), Keys.ENTER)
        driver.find_element_by_xpath("//input[@name='street[1]']").send_keys(
                                         '1test'+str(random.randrange(100)), Keys.ENTER)
        driver.find_element_by_xpath("//input[@name='street[0]']").send_keys(
                                         '1test'+str(random.randrange(100)), Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@name='region']")[0].send_keys(
                                        '1test'+str(random.randrange(100)), Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@name='city']")[0].send_keys(
                                       '1test'+str(random.randrange(100)), Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@name='postcode']")[0].send_keys(
                                       random.randrange(1000, 9999), Keys.ENTER)
        driver.find_element_by_xpath("//button[@data-role='opc-continue']").click()
        time.sleep(7)
        driver.find_element_by_xpath("//button[@value='Place Order']").click()
        time.sleep(5)
        assert "Success" in driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
