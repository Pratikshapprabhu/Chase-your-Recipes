import sqlite3 as sq
import hebbars_kitchen as hk
import timesofindia as ti
import yum_recipe as yr 


#returns list of [(name, recipe_id(link), image url)]
def search_recipe(search_term):
    return ("This is recipe", "https://this.is.recipe", "url")


def __init_database():
    con = sq.connect('test.db')
    con.execute(''' CREATE TABLE INDEX_TABLE
            (URL TEXT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                IMG_URL TEXT )''')
    con.execute(''' CREATE TABLE RECIPES
            (ID TEXT PRIMARY KEY NOT NULL,
                INGREDIENTS TEXT,
                RECIPE TEXT,
                DESCRIPTION TEXT,
                TAGS TEXT
                )''')
    con.commit()
    return con

def sync_database():
    con = __init_database()
    # sync all the sites recipes
    hk.scrapp_all("test.db")
    # ti.scrapp_all()
    # yr.scrapp_all()


#returns recipe object
#input:link of recipe
def get_recipe(recipe_id):
    # check site
    # scrap the site
    # update database for that single recipe.
    # return recipe object
    pass
