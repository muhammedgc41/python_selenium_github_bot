from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ElemanComTest:
    def __init__(self):
        self.options=webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)
        self.sr=webdriver.Chrome(options=self.options)
        self.sr.get("https://eleman360.com/")
        time.sleep(2)
        self.sr.maximize_window()
        self.execute()
    def ilanVerButton(self):    
        self.btn2=self.sr.find_element(By.XPATH, "/html/body/header[1]/div/div/div[1]/form/div/a/strong")
        time.sleep(3)
        self.btn2.click()
    def texboxMeslekYaz(self):    
        self.pozisyon=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[1]/input")
        time.sleep(1)
        self.pozisyon.send_keys("eleman")
        time.sleep(2)
    def btncinsiyet(self):
        self.btn2=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/select[1]")
        time.sleep(2)
        self.btn2.click()
    def btncinsiyetbay(self):
        self.bay=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/select[1]/option[2]")
        time.sleep(2)
        self.bay.click()
    def btnyas(self): 
        self.yas=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[2]/select[1]")
        time.sleep(2)
        self.yas.click()
    def btnyas20(self): 
        self.yas1=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[2]/select[1]/option[4]")
        time.sleep(2)
        self.yas1.click()
    def btnyas2(self): 
        self.yas2=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[2]/select[2]")
        time.sleep(2)
        self.yas2.click()
    def btnyas202(self): 
        self.yas3=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[2]/select[2]/option[1]")
        time.sleep(2)
        self.yas3.click()
    def textboxilandetayi(self): 
        self.sifre=self.sr.find_element(By.XPATH,"/html/body/section/div/div/div/div[2]/div/form/textarea[1]")
        time.sleep(2)
        self.sifre.send_keys("iş aramıyorum")
    def btnmaas(self): 
        time.sleep(2)
        self.sr.execute_script("window.scrollBy(0, 500);")
        self.maas=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/select[2]")
        time.sleep(2)
        self.maas.click()
    def btnmaas2(self): 
        self.maas2=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/select[2]/option[2]")
        time.sleep(2)
        self.maas2.click()
    def btncalisma(self): 
        self.calisma=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/select[3]")
        time.sleep(2)
        self.calisma.click()        
    def btncalisma2(self): 
        self.calisma2=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/select[3]/option[3]")
        time.sleep(2)
        self.calisma2.click()
    def btntiklama(self): 
        self.tiklama=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[3]/div/div/label[3]/input")
        time.sleep(2)
        self.tiklama.click()
    def btnsehir(self): 
        self.sr.execute_script("window.scrollBy(0, 500);")
        self.sehir=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[5]/select[1]")
        time.sleep(2)
        self.sehir.click()
    def btnsehir1(self): 
        self.sehir1=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[5]/select[1]/option[77]")
        time.sleep(2)
        self.sehir1.click()
    def btnsehir2(self): 
        self.sehir2=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[5]/select[2]")
        time.sleep(2)
        self.sehir2.click()
    def btnsehir3(self): 
        self.sehir3=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[5]/select[2]/option[10]")
        time.sleep(2)
        self.sehir3.click()
    def btnfirma(self): 
        self.firma=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[6]/input")
        time.sleep(1)
        self.firma.send_keys("ülker")
    def btnadres(self): 
        self.adres=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/textarea[2]")
        time.sleep(1)
        self.adres.send_keys("iskele mahallesi ibibik 8.sokak no:18 daire:2 van/merkez")
    def btnaday(self):
        self.aday=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[7]/input")
        time.sleep(1)
        self.aday.send_keys("1.kişi")
    def btntelefon(self): 
        self.sr.execute_script("window.scrollBy(0, 500);")
        self.phone=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[8]/div/input[1]")
        time.sleep(1)
        self.phone.send_keys("5065142509")
    def btnsaat(self): 
        self.saat=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[10]/select[1]")
        time.sleep(2)
        self.saat.click()
    def btnsaat1(self): 
        self.saat1=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[10]/select[1]/option[1]")
        time.sleep(2)
        self.saat1.click()
    def btnsaat2(self): 
        self.saat2=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[10]/select[2]")
        time.sleep(2)
        self.saat2.click()
    def btnsaat3(self): 
        self.saat3=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[10]/select[2]/option[4]")
        time.sleep(2)
        self.saat3.click()
    def btnwebsite(self): 
        self.web=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[11]/input")
        time.sleep(1)
        self.web.send_keys("web adresim bulunmamaktadır")
    def btnmail(self): 
        self.mail=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/div[12]/input[1]")
        time.sleep(1)
        self.mail.send_keys("aciksemih407@gmail.com")
    def btnokuma1(self): 
        self.sr.execute_script("window.scrollBy(0, 500);")
        self.okuma1=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/label[2]/input")
        time.sleep(2)
        self.okuma1.click()
    def btnokuma1onay(self): 
        self.okuma1onay=self.sr.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/button")
        time.sleep(2)
        self.okuma1onay.click()
    def btnokuma2(self): 
        self.okuma2=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/label[3]/input")
        time.sleep(2)
        self.okuma2.click()
    def btnokuma2onay(self): 
        self.okuma2onay=self.sr.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button")
        time.sleep(2)
        self.okuma2onay.click()
    def btnokuma3(self): 
        self.okuma3=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/label[4]/input")
        time.sleep(2)
        self.okuma3.click()
    def btnokuma4(self): 
        self.buton=self.sr.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/form/input")
        time.sleep(2)
        self.buton.click()
    def execute(self):
        self.ilanVerButton()
        self.texboxMeslekYaz()
        self.btncinsiyet()
        self.btncinsiyetbay()
        self.btnyas()
        self.btnyas20()
        self.btnyas2()
        self.btnyas202()
        self.textboxilandetayi()
        self.btnmaas()
        self.btnmaas2()
        self.btncalisma()
        self.btncalisma2()
        self.btntiklama()
        self.btnsehir()
        self.btnsehir1()
        self.btnsehir2()
        self.btnsehir3()
        self.btnfirma()
        self.btnadres()
        self.btnaday()
        self.btntelefon()
        self.btnsaat()
        self.btnsaat1()
        self.btnsaat2()
        self.btnsaat3()
        self.btnwebsite()
        self.btnmail()
        self.btnokuma1()
        self.btnokuma1onay()
        self.btnokuma2()
        self.btnokuma2onay()
        self.btnokuma3()
        self.btnokuma4()
ElemanComTest()