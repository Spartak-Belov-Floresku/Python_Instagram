from src.browser import Browser
from src.hashtag import HashTag

class Instagram():
    def __init__(self, username, password, hash_tag):
        self.__driver_browser = ""
        
        self.__browser = Browser(username, password)
        self.__Method_Browser()

        self.__hashtag = HashTag(self.__driver_browser, hash_tag)
        self.__Method_Hash_Tag()
        
    def __Method_Browser(self):
        self.__browser.Start_Browser()
        self.__browser.Open_LogPage()
        self.__driver_browser = self.__browser.Login_To_Account()

    def __Method_Hash_Tag(self):
        self.__hashtag.Open_Hashtag()
        self.__hashtag.Scroll_Browser()
        self.__hashtag.Get_Href_Img()
        self.__hashtag.Liked_Pic()
