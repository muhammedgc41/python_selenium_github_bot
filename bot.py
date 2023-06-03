from random import randint
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GithubTest:
    def __init__(self):
        self.url = "https://github.com/"

        # User agent bilgisini değiştirmek için Chrome seçeneklerini ayarlayın
        self.chrome_options = Options()
        self.chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

        # WebDriver'ı oluştururken Chrome seçeneklerini kullanın
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(randint(4, 6))
        self.execute()
        input("Press enter to exit")

    def loginPage(self):
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")       
        loginButton.click()       
        time.sleep(randint(4,6))

    def girisyapkullaniciadi(self):
        self.kullaniciAdi=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]")        
        self.kullaniciAdi.send_keys("salvougr1@gmail.com")       
        time.sleep(randint(4,6))

    def girisyapsifre(self):
        self.sifre=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]")
        self.sifre.send_keys("Dagac-1903bjk")
        time.sleep(randint(4,6))

    def girisyapbutton(self):
        self.button1=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]").click()
        time.sleep(randint(4,6))

    def imagebutton(self):
        imageButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details/summary/img")
        imageButton.click()
        time.sleep(randint(4,6))   

    def respositioresbutton(self):
        resButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details/details-menu/a[2]")
        resButton.click()
        time.sleep(randint(4,6)) 

    def pythongıthubbotbutton(self):
        githubbotButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[1]/div[1]/div[1]/h3/a")
        githubbotButton.click()
        time.sleep(randint(4,6))  

    def addfilebutton(self):
        addfileButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[2]/details/summary")
        addfileButton.click()
        time.sleep(randint(4,6))     

    def createbutton(self):
        newfileButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[2]/details/div/ul/li[3]/form/button")
        newfileButton.click()
        time.sleep(randint(4,6)) 

    def nameyourfile(self):
        self.yourfile = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[2]/div[1]/div/div/main/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/span[2]/input")
        self.yourfile.send_keys("muhammed.erg")
        time.sleep(randint(4, 6))     

    def edit(self):
        self.edit=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[2]/div[1]/div/div/main/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[5]/div[1]/div/div/div/div[5]/div/pre")
        self.edit.send_keys("<script> alert= merhaba dünya </script>")
        time.sleep(randint(4,6))  

    def commitbutton(self):
        commitButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[2]/div[1]/div/div/main/div[2]/div/div[3]/div[1]/div[2]/button/span/span")
        commitButton.click()
        time.sleep(randint(4,6))   

    def commitmesage(self):
        self.commitmessage=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div/div[2]/form/div[1]/span/input")
        self.commitmessage.send_keys("")
        time.sleep(randint(4,6))   

    def commitchanges(self):
        changesButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div/div[3]/button[2]")
        changesButton.click()
        time.sleep(randint(4,6)) 

    def githublogo(self):
        logoButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[1]/a")
        logoButton.click()
        time.sleep(randint(4,6)) 

    def searchorjump(self):
        jumpButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[3]/qbsearch-input/div[1]/button/span")
        jumpButton.click()
        time.sleep(randint(4,6))   

    def kullaniciara(self):
        self.kullanici=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[3]/qbsearch-input/div[1]/div/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input")
        self.kullanici.send_keys("nedimkacan",Keys.ENTER)
        time.sleep(randint(4,6)) 

    def users(self):
        usersButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/react-app/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div/ul/li[1]/ul/li[6]/a/div/div/span[1]")
        usersButton.click()
        time.sleep(randint(4,6))     

    def ndmkcn(self):
        nedimkacanButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/react-app/div/div/div/div[1]/div/div/main/div[2]/div/div[1]/div[4]/div/div/div/div/div[1]/div[2]/h3/div/a[1]/span")
        nedimkacanButton.click()
        time.sleep(randint(4,6))   

    def ndmkcnresp(self):
        nedimkacanrespButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div[1]/div/div/div[2]/div/nav/a[2]")
        nedimkacanrespButton.click()
        time.sleep(randint(4,6))    
        
    def star(self):
        starButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[3]/div[2]/div[1]/div[2]/form/button")
        starButton.click()
        time.sleep(randint(4,6))                        


    def execute(self):
        self.loginPage()
        self.girisyapkullaniciadi()
        self.girisyapsifre()
        self.girisyapbutton()
        self.imagebutton()
        self.respositioresbutton()
        self.pythongıthubbotbutton()
        self.addfilebutton()
        self.createbutton()
        self.nameyourfile()
        self.edit()
        self.commitbutton()
        self.commitmesage()
        self.commitchanges()
        self.githublogo()
        self.searchorjump()
        self.kullaniciara()
        self.users()
        self.ndmkcn()
        self.ndmkcnresp()
        self.star()
GithubTest()
