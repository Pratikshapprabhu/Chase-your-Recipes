#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import requests
from ..models import RecipeStore, RecipeIndex
from urllib.parse import urlparse

class ArticleError(Exception):
    pass
    
def get_name(sp):
    return sp.find('header', class_='td-post-title').h1.text

def get_dis(sp):
    return sp.find('div', class_= 'td-post-content tagdiv-type').p.text

def get_ing(sp):
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

def get_rec(sp):
    y = []
    try:
        instructions = sp.find('div', class_='wprm-recipe-instruction-group').ul.find_all('div')
    except AttributeError:
        print("Couldn't get recipe")
        return []
    for i in instructions:
        y.append(i.getText())
    return y
    
def get_img(sp):
    try:
        return sp.find('img',class_ = 'entered lazyloaded')['src']
    except TypeError:
        return ""

def get_article(link):
    print(f"parsing {link}")
    content = requests.get(link)
    sp = bs(content.text,'lxml')
    # if the page doesn't exist
    try:
        name = get_name(sp)
    except AttributeError:
        raise ArticleError
    des = get_dis(sp)
    ing = get_ing(sp)
    rec = get_rec(sp)
    name = name.strip() if name else ""
    des = des.strip() if des else ""
    ing = ing if ing else ""
    img = get_img(sp) if ing else ""
    url_obj = urlparse(link)
    domain = url_obj.hostname
    store_obj = RecipeStore(url=link,ingredients=ing,preparation=rec,desc=des)
    store_obj.save()
    index = RecipeIndex(url=store_obj,recipe_name=name,img_url=img,domain=domain)    
    index.save()

def scrape_all():
    link = "https://hebbarskitchen.com/"
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
                get_article(lnk)
            except ArticleError:
                continue
        
            
if(__name__ == "__main__"):
    art = scrape_all()

