from typing_extensions import Self


class Article:
    name = None
    ingredients = None
    procedure = None
    description = None
    image_link = None
    
    def __init__(self,name,image_link,procedure,ingredients='',description='') -> Self:
        self.name = name
        self.ingredients = ingredients
        self.procedure = procedure
        self.description = description
        self.image_link = image_link