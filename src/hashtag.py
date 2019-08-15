from selenium.webdriver.common.by import By
import time

from src.database import DB

class HashTag():
    def __init__(self, browser, hash_tag):
        self.__browser = browser
        self.__hash_tag = hash_tag
        self.__img_list = ""

    def closeBrowser(self):
        self.__browser.close()

    def Open_Hashtag(self):
        self.__browser.get("https://www.instagram.com/explore/tags/"+self.__hash_tag+"/")
        self.__Sec(3)

    def Scroll_Browser(self):
        for i in range(0, 3):
            print('scroll # '+ str(i+1))
            self.__browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.__Sec(2)

    def Get_Href_Img(self):
        try:
            tags_a = self.__browser.find_elements_by_tag_name('a')
            img_hrefs = [tag_a.get_attribute('href') for tag_a in tags_a]
            self.__img_list = [href for href in img_hrefs]
            print('Photos '+ str(len(self.__img_list)))
        except Exception as e:
            print("Error in class HashTag method Get_Href_Img: "+str(e))
            return

    def Liked_Pic(self):
        for img_href in self.__img_list:
            if self.__Check_Href_To_Img(img_href) == -1:
                continue
            if self.__Check_DB(img_href):
                self.__browser.get(img_href)
                self.__browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    self.__Sec(10)
                    self.__browser.find_element(By.XPATH, '//span[@aria-label="Like"]').click()
                    print("Img has been liked")
                    self.__Sec(10)
                except Exception as e:
                    print("Error: "+str(e))
                    self.__Sec(2)

        self.closeBrowser()
        print("all urls done")
        return

    def __Check_Href_To_Img(self, url):
        base_url = "https://www.instagram.com/p/"
        return url.find(base_url)

    def __Check_DB(self, href):
        db = DB(href)
        return db.Check_DB()
        
        

    def __Sec(self,sec):
        time.sleep(sec)
