from instaUser import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(5)
        usernameInput = self.browser.find_element(By.NAME, 'username') 
        passwordInput = self.browser.find_element(By.NAME, 'password') 

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        

    def getFollowers(self):
        time.sleep(5)
        self.browser.get(
            f"https://www.instagram.com/buzzfeedtasty/followers/")
        
        time.sleep(2)
        dialog = self.browser.find_element(
            By.CSS_SELECTOR, "div[role=dialog] ul")
        for i in range(10):
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(2)
            
        followerCount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))
        print(f"First count: {followerCount}")
        
    def follow(self):
        all_buttons = self.browser.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.browser.find_element(
            By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.getFollowers()
instgrm.follow()