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
        time.sleep(6)
        product_name = driver.find_element_by_xpath("//form[@data-product-sku='2034866R']/ancestor::div[4]/strong/a").text
        driver.find_element_by_xpath("//form[@data-product-sku='2034866R']/button").click()
        driver.find_element_by_xpath("//a[@class='action showcart']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@id='top-cart-btn-checkout']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//button[@data-role='proceed-to-checkout']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//a[@class='continue-guest']").click()
        time.sleep(7)
        lastname = 'test'+str(random.randrange(100))
        driver.find_element_by_xpath("//input[@name='lastname']").send_keys(lastname, Keys.ENTER)
        firstname = 'test'+str(random.randrange(100))
        driver.find_element_by_xpath("//input[@name='firstname']").send_keys(firstname, Keys.ENTER)
        username = 'test'+str(random.randrange(10000))+'@gmail.com'
        driver.find_elements_by_xpath("//input[@name='username']")[1].send_keys(username, Keys.ENTER)
        telephone = ' 77 '+str(random.randint(100000, 999999))
        driver.find_element_by_xpath("//input[@name='telephone']").send_keys(telephone, Keys.ENTER)
        street1 = '1test'+str(random.randrange(100))
        driver.find_element_by_xpath("//input[@name='street[1]']").send_keys(street1, Keys.ENTER)
        street2 = '1test'+str(random.randrange(100))
        driver.find_element_by_xpath("//input[@name='street[0]']").send_keys(street2, Keys.ENTER)
        driver.find_elements_by_xpath("//input[@name='postcode']")[0].send_keys(
                                       random.randrange(1000, 9999), Keys.ENTER)
        driver.find_element_by_xpath("//button[@data-role='opc-continue']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@value='Place Order']").click()
        time.sleep(7)
        assert "Success" in driver.title
        test_name = firstname+' '+lastname
        test_street = street2+' '+street1
        test_telephone = '+374'+telephone
        name = driver.find_element_by_xpath("//div[@class='shipTo info-pay-block pay-product-info']/div[2]/div[2]/span").text
        street = driver.find_element_by_xpath("//div[@class='shipTo info-pay-block pay-product-info']/div[3]/div[2]/span").text
        telephone = driver.find_element_by_xpath("//div[@class='shipTo info-pay-block pay-product-info']/div[4]/div[2]/span").text
        test_product = driver.find_element_by_xpath("//div[@class='description-prod-pay']/div[2]").text
        assert product_name == test_product
        assert name == test_name
        assert street == test_street
        assert telephone == test_telephone

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
