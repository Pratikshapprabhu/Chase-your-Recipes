from bs4 import BeautifulSoup as bs
import requests


class Article:
    def get_name(self, sp):
        return sp.find('div',class_ = 'tab_search clearfix').h2.text

    def get_ing(self, sp):
        return sp.find('div',id = 'ingredata').ul.text

    def get_rec(self, sp):
        return sp.find('div',class_= 'recipetabsdata').text

    def __init__(self, link):
        content = requests.get(link)
        sp = bs(content.text, 'lxml')
        self.name = self.get_name(sp)
        self.ing = self.get_ing(sp)
        self.rec = self.get_rec(sp)



if (__name__ == "__main__"):
    content = requests.get('https://recipes.timesofindia.com/chefs/pankaj-bhadouria-recipes')
    sp = bs(content.text, 'lxml')
    link = sp.find('div', id='collectionresults').div
    links = []

    while link:
        try:
            links.append(link.div.span.a["href"])
        except TypeError:
            break
        link = link.next_sibling
    for link in links:
        art = Article(link)

    print("NAME:\n" + art.name)
    #print("DESCRIPTION:\n" + art.des)
    print("INGREDIENT: ")
    print(art.ing)
    print("RECIPE: ")
    for i in (art.rec):
        print(art.rec)
