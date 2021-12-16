#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

class ArticleError(Exception):
    pass
    
class Article:
    def get_name(self,sp):
        return sp.find('header', class_='td-post-title').h1.text
    def get_dis(self,sp):
        return sp.find('div', class_= 'td-post-content tagdiv-type').p.text
    def get_ingredients(self,sp):
        ingredients = []
        ingredient_ul = sp.find('ul',class_ ='wprm-recipe-ingredients')
        if not ingredient_ul:
            print("couldn't able to get ingredients")
            return ''
        for i in ingredient_ul.find_all('li',class_ = 'wprm-recipe-ingredient'):
            amount = i.find('span', class_='wprm-recipe-ingredient-amount')
            amount = amount.getText() if amount else ""
            unit = i.find('span', class_='wprm-recipe-ingredient-unit')
            unit = unit.getText() if unit else ""
            name = i.find('span', class_='wprm-recipe-ingredient-name')
            name = name.getText() if name else ""
            ingredients.append(' '.join((amount,unit,name)))
        return ingredients
    def get_tag(self,sp):
        return ''
    def get_rec(self,sp):
        y = []
        try:
            instructions = sp.find('div', class_='wprm-recipe-instruction-group').ul.find_all('div')
        except AttributeError:
            print("Couldn't get recipe")
            return []
        for i in instructions:
            y.append(i.getText())
        return y

    def __init__(self,link):
        print(f"parsing {link}")
        content = requests.get(link)
        sp = bs(content.text,'lxml')
        # if the page doesn't exist
        try:
            name = self.get_name(sp)
        except AttributeError:
            raise ArticleError
        des = self.get_dis(sp)
        ing = self.get_ingredients(sp)
        self.tag = self.get_tag(sp)
        self.rec = self.get_rec(sp)
        self.name = name.strip() if name else ""
        self.des = des.strip() if des else ""
        self.ing = ing if ing else ""

    def __str__(self):
        return f"name: {self.name}\ndescription: {self.des}\ningredients: {self.ing}\nrecipe: {self.rec}\ntags:{self.tag}"


if(__name__ == "__main__"):
    link = "https://hebbarskitchen.com/"
    df = pd.DataFrame(columns=['Name','Description','Ingredients','Recipe'])
    df.to_csv('data/web_data.csv', index=False)
    while(link):
        page = requests.get(link)
        soup = bs(page.text, 'lxml')
        div = soup.find("div", id="tdi_73").div
        link = soup.find('a', attrs={"aria-label":"next-page"})["href"]
        links = []
        while div:
            if div == '\n':
                div = div.next_sibling
                continue
            lnk = div.find_all("a")[0]["href"]
            links.append(lnk)
            div = div.next_sibling
        for lnk in links:
            try:
                art = Article(lnk)
            except ArticleError:
                continue
            data = [art.name, art.des, art.ing, art.rec]
            df = pd.DataFrame([data],columns=['Name','Description','Ingredients','Recipe'])
            df.to_csv('data/web_data.csv', mode="a", index=False, header=False)

