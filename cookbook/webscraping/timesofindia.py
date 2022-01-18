from bs4 import BeautifulSoup as bs
import requests
from ..models import RecipeStore, RecipeIndex
from urllib.parse import urlparse

def get_name(sp):
    return sp.find('h1',class_ = 'nheadingrs').text

def get_ing(sp):
    return sp.find('div',id = 'ingredata').text

def get_rec(sp):
    return sp.find('div',class_= 'steps_listings clearfix').text

def get_des(sp):
    return sp.find('div', class_ = 'summeryhtcontentin').text

def get_img(sp):
    return sp.find('div',class_='topfeature ntopfeaturers clearfix').img['src']
    
def get_article(link):
    content = requests.get(link)
    sp = bs(content.text, 'lxml')
    name = get_name(sp)
    ing = get_ing(sp)
    rec = get_rec(sp)
    des = get_des(sp)
    img = get_img(sp)
    url_obj = urlparse(link)
    domain = url_obj.hostname
    store_obj = RecipeStore(url=link,ingredients=ing,preparation=rec,desc=des)
    store_obj.save()
    index = RecipeIndex(url=store_obj,recipe_name=name,img_url=img,domain=domain)    
    index.save()

def scrape_all():
    content = requests.get('https://recipes.timesofindia.com/recipes/')
    sp = bs(content.text, 'lxml')
    lnk_list = sp.find_all('div', class_='mustTry_left recipemainli')
    links = []

    for link in lnk_list:
        try:
            links.append(link.a["href"])
        except TypeError:
            pass
    for link in links:
        art = get_article(link)
        print(link)
        

if (__name__ == "__main__"):
    art = scrape_all()
   
