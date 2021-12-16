from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import os

class Article:
    def get_name(self, sp):
        return sp.find('h1',class_ = 'nheadingrs').text

    def get_ing(self, sp):
        return sp.find('div',id = 'ingredata').text

    def get_rec(self, sp):
        return sp.find('div',class_= 'steps_listings clearfix').text

    def get_des(self, sp):
        return ''

    def __init__(self, link):
        content = requests.get(link)
        sp = bs(content.text, 'lxml')
        self.name = self.get_name(sp)
        self.ing = self.get_ing(sp)
        self.rec = self.get_rec(sp)
        self.des = self.get_des(sp)


if (__name__ == "__main__"):
    content = requests.get('https://recipes.timesofindia.com/recipes/')
    sp = bs(content.text, 'lxml')
    lnk_list = sp.find_all('div', class_='mustTry_left recipemainli')
    links = []
    if not os.path.exists('project/webscraping/data/web_data.csv'):
        df = pd.DataFrame(columns=['Name','Description','Ingredients','Recipe'])
        df.to_csv('data/web_data.csv', index=False)
    for link in lnk_list:
        try:
            links.append(link.a["href"])
        except TypeError:
            pass
    for link in links:
        art = Article(link)
        print(link)
        data = [art.name, art.des, art.ing, art.rec]
        df1 = pd.DataFrame([data])
        df1.to_csv('data/web_data.csv', mode="a", index=False, header=False)
