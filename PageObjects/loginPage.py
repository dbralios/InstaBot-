from PageObjects.basePage import BasePage
from PageObjects.locators import LogInPageLocators
from selenium.webdriver.common.keys import Keys
import time

class LogInPage(BasePage):

    def visit(self):
        BasePage.visit(self, 'http://www.instagram.com/accounts/login')
        
    def login(self, username, password):
       assert "Login" in self.driver.title
       self.set_text(LogInPageLocators.USER, username)
       self.set_text(LogInPageLocators.PASS, password)
       self.wait(5)
       self.send_keys(LogInPageLocators.PASS, Keys.RETURN)
       self.wait(5)
