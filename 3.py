from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://admin:admin123@staging.shopia.com")
        driver.maximize_window()

        time.sleep(5)
        driver.find_element_by_xpath("//form[@data-product-sku='2034866R']/button").click()
        time.sleep(4)
        driver.get("https://staging.shopia.com/pluzz-p5130-32mb-ram-32mb-rom-1-3-megapixel-camera-2-4-inch-display-blue.html")
        time.sleep(5)
        # driver.find_element_by_xpath("//label[@for='economy_economy']").click()
        # time.sleep(5)
        # continue_link = driver.find_element_by_link_text('Shipping methods can')
        # time.sleep(5)
        # driver.find_element_by_xpath("//body").click()
        # # driver.find_elements_by_xpath("//div[@class='fancybox-overlay fancybox-overlay-fixed']").click()
        # driver.find_element_by_xpath("//a[@title='Close']").click()
        # logging.warning(driver.find_elements_by_xpath("//button[@title='Add To Cart']"))
        driver.find_element_by_xpath("//button[@title='Add To Cart']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='action showcart']").click()
        driver.find_element_by_xpath("//button[@id='top-cart-btn-checkout']").click()
        time.sleep(7)
        elem = driver.find_element_by_xpath("//input[@value='economy_economy']")
        ActionChains(driver).move_to_element(elem).click().perform()

        driver.find_element_by_xpath("//button[@data-role='proceed-to-checkout']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//a[@class='continue-guest']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@name='lastname']").send_keys(
                                       'test'+str(random.randrange(100)), Keys.ENTER)
        driver.find_element_by_xpath("//input[@name='firstname']").send_keys(
                                       '1test'+str(random.randrange(100)), Keys.ENTER)
        driver.find_elements_by_xpath("//input[@name='username']")[1].send_keys(
                                       'test'+str(random.randrange(10000))+'@gmail.com', Keys.ENTER)
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
        time.sleep(10)
        assert "Success" in driver.title
        logging.warning(driver.find_elements_by_xpath("//span[@class='price']")[1].text)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
