from bs4 import BeautifulSoup as bs
import requests
import articles

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
    return articles.Article(name,img,rec,ing,des)

def scrap_all():
    content = requests.get('https://recipes.timesofindia.com/recipes/')
    sp = bs(content.text, 'lxml')
    lnk_list = sp.find_all('div', class_='mustTry_left recipemainli')
    links = []
    recipes = []
    for link in lnk_list:
        try:
            links.append(link.a["href"])
        except TypeError:
            pass
    for link in links:
        art = get_article(link)
        print(link)
        recipes.append(art)
    return recipes

if (__name__ == "__main__"):
    art = scrap_all()
    #for a in art:
    #   dump to databse(a)   
