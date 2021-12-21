from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import os

class Article:
    def get_name(self, sp):
        return sp.find('div',class_ = 'imo').span.text

    def get_ing(self, sp):
        div = sp.find('div',class_ = 'ingrdnt').find_all('p')[5:]
        return list(map(lambda x:x.text,div))

    def get_rec(self, sp):
        div = sp.find('div',class_= 'prptn').find_all('p')
        return list(map(lambda x:x.text,div))
        
    def get_des(self, sp):
        return ''

    def get_img(self, link):
        return link.find('img')['src']

    def __init__(self, link):
        content = requests.get(link)
        sp = bs(content.text, 'lxml')
        self.name = self.get_name(sp)
        self.ing = self.get_ing(sp)
        self.rec = self.get_rec(sp)
        self.des = self.get_des(sp)
        self.img = self.get_img(link)


if (__name__ == "__main__"):
    content = requests.get('https://www.yumrecipe.in/')
    sp = bs(content.text, 'lxml')
    lnk_list = sp.find_all('div', class_='latest-feed')
    links = []
    #if file doesnot exist create the file
    if not os.path.exists('project/webscraping/data/web_data.csv'):
        df = pd.DataFrame(columns=['Name','Domain','Link','Description','Ingredients','Recipe','Image'])
        df.to_csv('data/web_data.csv', index=False)
        
    for link in lnk_list:
        lnk = link.find('ul').li.span.div.a["href"]
        links.append(lnk)
    for link in links:
        art = Article(link)
        print(link)
        data = [art.name, "Yum Recipe", link, art.des, "\n".join(art.ing), "\n".join(art.rec), art.img]
        df2 = pd.DataFrame([data])
        df2.to_csv('data/web_data.csv', mode="a", index=False, header=False)
