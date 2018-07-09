from PageObjects.basePage import BasePage
from PageObjects.locators import ProfilePageLocators

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ProfilePage(BasePage):   
    
    def __init__(self, driver, user):
        BasePage.driver = driver
        self.username = user

    def visit(self):
        BasePage.visit(self, 'http://www.instagram.com/' + self.username)

    def is_title_matches(self):
        return self.username in self.driver.title

    def open_followers_dialog(self):
        self.focus_click_element(ProfilePageLocators.FOLLOWERS)

    def open_posts_dialog(self):
        return self.click_element(ProfilePageLocators.POSTS)
        
    class FollowersDialog(BasePage):
    
        def getFollowers(self):
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ARROW_DOWN)
            actions.send_keys(Keys.ARROW_DOWN)
            for _ in range(250):                      
                actions.perform()
                self.wait()
       
            followers_elems = self.driver.find_elements(*ProfilePageLocators.FollowersDialogLocators.FOLLOWER_ELEM)

            return [e.text for e in followers_elems]
        
        def close(self):
            self.click_element(ProfilePageLocators.FollowersDialogLocators.CLOSE)
    
    class PostsDialog(BasePage):
        
        def like(self):
            self.click_element(ProfilePageLocators.PostsDialogLocators.LIKE)

        def next(self):
            self.click_element(ProfilePageLocators.PostsDialogLocators.NEXT)

        def close(self):
            self.click_element(ProfilePageLocators.PostsDialogLocators.CLOSE)
