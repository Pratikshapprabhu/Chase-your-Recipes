from bs4 import BeautifulSoup as bs
import requests
from .articles import Article

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
    return link.find('img')['src']

def get_article(link):
    content = requests.get(link)
    sp = bs(content.text, 'lxml')
    name = get_name(sp)
    ing = get_ing(sp)
    rec = get_rec(sp)
    des = get_des(sp)
    img = get_img(link)
    return Article(link,name,img,rec,ing,des)

def scrape_all():
    content = requests.get('https://www.yumrecipe.in/')
    sp = bs(content.text, 'lxml')
    lnk_list = sp.find_all('div', class_='latest-feed')
    links = []
    recipes = []
    for link in lnk_list:
        lnk = link.find('ul').li.span.div.a["href"]
        links.append(lnk)
    for link in links:
        art = get_article(link)
        print(link)
        recipes.append(art)
    return recipes

if (__name__ == "__main__"):
    art = scrape_all()