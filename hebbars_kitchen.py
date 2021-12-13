#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import logging
import requests
    
class Article:
    def get_name(self,sp):
        return sp.find('header', class_='td-post-title').h1.text
    def get_dis(self,sp):
        return sp.find('div', class_= 'td-post-content tagdiv-type').p.text
    def get_ingredients(self,sp):
        ingredients = []
        ingredient_ul = sp.find('ul',class_ ='wprm-recipe-ingredients')
        if not ingredients:
            logging.info("couldn't able to get ingredients")
            return
        for i in ingredient_ul.find_all('li',class_ = 'wprm-recipe-ingredient'):
            amount = i.find('span', class_='wprm-recipe-ingredient-amount')
            amount = amount.getText() if amount else None
            unit = i.find('span', class_='wprm-recipe-ingredient-unit')
            unit = unit.getText() if unit else None
            name = i.find('span', class_='wprm-recipe-ingredient-name')
            name = name.getText() if name else None
            ingredients.append((amount,unit,name))
        return ingredients
    def get_tag(self,sp):
        return ''
    def get_rec(self,sp):
        y = []
        try:
            instructions = sp.find('div', class_='wprm-recipe-instruction-group').ul.find_all('div')
        except AttributeError:
            logging.info("Couldn't get recipe")
            return
        for i in instructions:
            y.append(i.getText())
        return y

    def __init__(self,link):
        content = requests.get(link)
        sp = bs(content.text,'lxml')
        name = self.get_name(sp)
        des = self.get_dis(sp)
        ing = self.get_ingredients(sp)
        self.tag = self.get_tag(sp)
        self.rec = self.get_rec(sp)
        self.name = name.strip() if name else None
        self.des = des.strip() if des else None
        self.ing = ing.strip() if ing else None

    def __str__(self):
        return f"name: {self.name}\ndescription: {self.des}\ningredients: {self.ing}\nrecipe: {self.rec}\ntags:{self.tag}"


if(__name__ == "__main__"):
    #art = Article('https://hebbarskitchen.com/poha-paratha-recipe-poha-aloo-ke-roti/')
    link = "https://hebbarskitchen.com/"
    page = requests.get(link)
    soup = bs(page.text, 'lxml')
    div = soup.find("div", id="tdi_73").div
    links = []
    while div:
        if div == '\n':
            div = div.next_sibling
            continue
        lnk = div.find_all("a")[0]["href"]
        links.append(lnk)
        div = div.next_sibling
    data = []
    for lnk in links:
        art = Article(lnk)
        print(art)
        print("-----------------")

