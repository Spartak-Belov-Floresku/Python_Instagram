from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class Browser():
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__driver = ""

    def Start_Browser(self):
         try:
             self.__driver = webdriver.Firefox(executable_path="geckodriver")
             self.__driver.get("https://www.instagram.com/")
             self.__Sec(3)
         except Exception as e:
             print("Browser error -> ",str(e))
             return
        
         
    def Open_LogPage(self):
        log_but = self.__driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        log_but.click()
        self.__Sec(3)
        return self.__driver

    def Login_To_Account(self):
        user_name = self.__driver.find_element_by_xpath("//input[@name='username']")
        user_name.clear()
        user_name.send_keys(self.__username)
        password = self.__driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.__password)
        password.send_keys(Keys.RETURN)
        self.__Sec(10)
        return self.__driver

    def __Sec(self,sec):
        time.sleep(sec)
