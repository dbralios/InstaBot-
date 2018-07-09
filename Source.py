import selenium.webdriver as webdriver
from PageObjects.loginPage import LogInPage
from PageObjects.profilePage import ProfilePage
import time

driver = webdriver.Edge('chromedriver.exe')
page = LogInPage(driver)
page.visit()
page.login('user', 'pass')

page = ProfilePage(driver, 'user')
page.visit()

page.open_followers_dialog()
fd = page.FollowersDialog(driver)
list = fd.getFollowers()

for e in list:
    pg = ProfilePage(driver, e)
    pg.visit()
    time.sleep(1)
    pg.open_posts_dialog()
    pd = pg.PostsDialog(driver)
    time.sleep(2)
    for _ in range(5):
        time.sleep(1)
        pd.like()
        time.sleep(1)
        pd.next()
    pd.close()
