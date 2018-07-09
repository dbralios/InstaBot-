from selenium.webdriver.common.by import By

class MainPageLocators(object):

    LOGIN_BUTTON = (By.LINK_TEXT, 'Log in')

class LogInPageLocators(object):

    USER = (By.NAME, 'username')
    PASS = (By.NAME, 'password')

class ProfilePageLocators(object):

    POSTS = (By.XPATH, '//a[contains(@href,"/p/")]')
    FOLLOWERS = (By.PARTIAL_LINK_TEXT, 'followers')

    class FollowersDialogLocators(object):

        CLOSE = (By.XPATH, '//button[text()="Close"]')
        FOLLOWER_ELEM = (By.XPATH, '//li/div/div/div/div/a')

    class PostsDialogLocators(object):

        CLOSE = (By.XPATH, '//button[text()="Close"]')
        LIKE = (By.XPATH, '//span[text()="Like"]')
        NEXT = (By.PARTIAL_LINK_TEXT, 'Next')

