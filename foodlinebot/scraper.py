from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests

#美食抽象類別
class Food(ABC):

    def __init__(self, area):
        self.area = area  #地區
    
    @abstractmethod
    def scrape(self):
        pass

#愛食記爬蟲
class IFood(Food):

    def scrape(self):
        print("1")
        response = requests.get("https://ifoodie.tw/explore/"+self.area+"/list?opening=true&sortby=rating")
        print("2")
        soup = BeautifulSoup(response.content, "html.parser")
        print("3")
        cards = soup.find_all('div',{'class':'jsx-3440511973 restaurant-info'}, limit=5)
        print("4")
        content = ""
        print("size=",len(cards))
        for card in cards:
            
            title = card.find("a",{'class':'jsx-3440511973 title-text'}).getText()
            print("title="+title)
            start = card.find("div",{'class':'jsx-1207467136 text'}).getText()
            print("start="+start)
            address = card.find("div",{'class':'jsx-3440511973 address-row'}).getText()
            print("address="+address)
            content += f"{title} \n {start}顆星 \n{address} \n\n"
            
            print("content="+content)
        return content