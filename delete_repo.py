import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class DeleteRepoGithub(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('https://github.com/')

    def test_login_and_delete_repo(self):

        user = 'USERNAME'
        pswd = 'PASSWORD'
        repo = "Repo-Test"


        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.username = self.driver.find_element(By.NAME, "login")
        self.password = self.driver.find_element(By.NAME, "password")
        self.login = self.driver.find_element(By.NAME, "commit")

        self.username.send_keys("{}".format(user))
        self.password.send_keys("{}".format(pswd))
        self.login.click()

        sleep(random.randrange(3,9))

        #navigate to the page of repositories
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/summary').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/details-menu/a[2]').click()

        sleep(random.randrange(3,9))

        #click one of the repositories
        self.driver.find_element(By.LINK_TEXT, "{}".format(repo)).click()
        self.driver.find_element(By.CSS_SELECTOR, '#settings-tab').click()
        self.driver.find_element(By.CSS_SELECTOR, '#dialog-show-repo-delete-menu-dialog > span > span').click()
        
        sleep(random.randrange(3,9))
        
        #I want to delete this repository
        self.driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span').click()
        #I have read and understand these effects
        self.driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span').click()

        sleep(random.randrange(3,9))

        #Type to confirm
        self.driver.find_element(By.XPATH, '//*[@id="verification_field"]').send_keys("{}/{}".format(user,repo))
        self.driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span').click()

        sleep(random.randrange(3,9))
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()