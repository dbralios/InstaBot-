from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all"""

    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def click_element(self, loc):
        if self.driver.find_elements(*loc):
            self.driver.find_element(*loc).click()

    def focus_click_element(self, loc):
        focus = ActionChains(self.driver)
        focus.click(self.driver.find_element(*loc))
        focus.perform()
        self.wait(2)
        focus.perform()
        self.wait(2)

    def set_text(self, loc, text):
        self.driver.find_element(*loc).send_keys(text)

    def send_keys(self, loc, key):
         self.driver.find_element(*loc).send_keys(key)

    def wait(self, wait_seconds=1):
        time.sleep(wait_seconds)

    