from curses import BUTTON_ALT
from random import randint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GithubTest:
    def __init__(self):
        self.url = "https://github.com/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(randint(2, 4))
        self.execute()
        input("Press enter to exit")

    def loginPage(self):
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")
        loginButton.click()
        time.sleep(randint(2, 4))
    
    def girisyapkullaniciadi(self):
        self.kullaniciAdi=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]")
        self.kullaniciAdi.send_keys("salvougr1@gmail.com")

    def girisyapsifre(self):
        self.sifre=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]")
        self.sifre.send_keys("Dagac-1903bjk")

    def girisyapbutton(self):
        self.button1=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[12]").click()
        


    def execute(self):
        self.loginPage()
        self.girisyapkullaniciadi()
        self.girisyapsifre()
        self.girisyapbutton()


GithubTest()
