import selenium.webdriver as webdriver
from PageObjects.loginPage import LogInPage
from PageObjects.profilePage import ProfilePage

driver = webdriver.Edge('C:\\chromedriver.exe')
page = LogInPage(driver)
page.visit()
page.login('user', 'pass')

page = ProfilePage('davidchoe')
page.visit()
