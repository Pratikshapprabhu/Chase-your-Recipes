from bs4 import BeautifulSoup as bs
import requests
from ..models import RecipeStore, RecipeIndex
from urllib.parse import urlparse

def get_name(sp):
    return sp.find('div',class_ = 'imo').span.text

def get_ing(sp):
    div = sp.find('div',class_ = 'ingrdnt').find_all('p')[5:]
    return list(map(lambda x:x.text,div))

def get_rec(sp):
    div = sp.find('div',class_= 'prptn').find_all('p')
    return list(map(lambda x:x.text,div))
        
def get_des(sp):
    return ''

def get_img(link):
    try:
        img_tag = link.find('img')['src']
    except TypeError:
        return ""
    return img_tag

def get_article(link):
    content = requests.get(link)
    sp = bs(content.text, 'lxml')
    name = get_name(sp)
    ing = get_ing(sp)
    rec = get_rec(sp)
    des = get_des(sp)
    img = get_img(link)
    url_obj = urlparse(link)
    domain = url_obj.hostname
    store_obj = RecipeStore(url=link,ingredients=ing,preparation=rec,desc=des)
    store_obj.save()
    index = RecipeIndex(recipe=store_obj,recipe_name=name,img_url=img,domain=domain)    
    index.save()

def scrape_all():
    content = requests.get('https://www.yumrecipe.in/')
    sp = bs(content.text, 'lxml')
    lnk_list = sp.find_all('div', class_='latest-feed')
    for link in lnk_list:
        lnk = link.find('ul').li.span.div.a["href"]
        print(lnk)
        get_article(lnk)

if (__name__ == "__main__"):
    scrape_all()
