from bs4 import BeautifulSoup as bs
import requests


class Article:
    def get_name(self, sp):
        return sp.find('h1',class_ = 'nheadingrs').text

    def get_ing(self, sp):
        return sp.find('div',id = 'ingredata').text

    def get_rec(self, sp):
        return sp.find('div',class_= 'steps_listings clearfix').text

    def __init__(self, link):
        content = requests.get(link)
        sp = bs(content.text, 'lxml')
        self.name = self.get_name(sp)
        self.ing = self.get_ing(sp)
        self.rec = self.get_rec(sp)



if (__name__ == "__main__"):
    content = requests.get('https://recipes.timesofindia.com/recipes/')
    sp = bs(content.text, 'lxml')
    lnk_list = sp.find_all('div', class_='mustTry_left recipemainli')
    links = []
    for link in lnk_list:
        try:
            links.append(link.a["href"])
        except TypeError:
            pass
    print(links)
    for link in links:
        art = Article(link)

        print("NAME:" + art.name)
    #print("DESCRIPTION:\n" + art.des)
        print("INGREDIENT: ",end = " ")
        print(art.ing)
        print("RECIPE: ")
        print(art.rec)
        print("----------------------------")
