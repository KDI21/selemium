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
        href = driver.find_element_by_xpath("//form[@data-product-sku='p5130BL']/ancestor::div[4]/strong/a").get_attribute('href')
        driver.get(href)
        time.sleep(5)
        driver.find_element_by_xpath("//label[@for='economy_economy']").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("//div[@class='fancybox-overlay fancybox-overlay-fixed']")
        ActionChains(driver).move_to_element_with_offset(elem, 250, 300).click().perform()
        time.sleep(2)
        driver.find_element_by_xpath("//button[@title='Add To Cart']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='action showcart']").click()
        driver.find_element_by_xpath("//button[@id='top-cart-btn-checkout']").click()
        time.sleep(7)
        elem = driver.find_element_by_xpath("//input[@value='economy_economy']")
        ActionChains(driver).move_to_element(elem).click().perform()
        time.sleep(3)
        economy = driver.find_element_by_xpath("//table[@class='data table totals']/tbody/tr[2]/th/span[2]").text
        assert economy == '(Economy)'



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
