from urllib.parse import urlparse

class Article:
    url = None
    name = None
    ingredients = None
    procedure = None
    description = None
    image_link = None
    #domain = None
    
    def __init__(self,url,name,image_link,procedure,ingredients='',description=''):
        self.url = url
        self.name = name
        self.ingredients = ingredients
        self.procedure = procedure
        self.description = description
        self.image_link = image_link
        url_obj = urlparse(url)
        self.domain = url_obj.hostname