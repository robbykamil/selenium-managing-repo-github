import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class CreateRepoGithub(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://github.com/")

    def test_login_and_create_Repo(self):
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.username = self.driver.find_element(By.NAME, "login")
        self.password = self.driver.find_element(By.NAME, "password")
        self.login = self.driver.find_element(By.NAME, "commit")

        self.username.send_keys("USERNAME")
        self.password.send_keys("PASSWORD")
        self.login.click()

        sleep(random.randrange(3,7))
        
        #navigate to page of create a new repo
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/aside/div/loading-context/div/div[1]/div/h2/a").click()

        #fill the data
        self.RepoName = self.driver.find_element(By.CSS_SELECTOR, '#react-aria-2').send_keys("Repo-Test")
        self.desc = self.driver.find_element(By.NAME, 'Description').send_keys("Created a repo for test with selenium")
        self.PrivateRepo = self.driver.find_element(By.XPATH, '//*[@id="react-aria-6"]').click()

        sleep(random.randrange(3,7))

        self.ButtonCreate = self.driver.find_element(By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive > div.application-main > main > react-app > div > div > form > div.Box-sc-g0xbh4-0.aBKvw > button > span > span').click()

        sleep(random.randrange(3,7))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
