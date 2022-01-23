from django.http.response import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template import context
from .models import RecipeIndex, RecipeStore
from math import ceil
from .webscraping import hebbars_kitchen as hk
from .webscraping import timesofindia as ti
from .webscraping import yum_recipe as yr
import threading

def search(request):
    query = request.POST.get("searchbar")
    if(not query):
        return HttpResponseBadRequest("Invalid search query") 
    results=RecipeIndex.objects.filter(recipe_name__contains=query)
    n= len(results)
    nSlides= n//4 + ceil((n/4) + (n//4))
    context = {'no_of_slides':nSlides, 'range':range(nSlides),"result":results}
    return render(request, "search_result.html", context)

def home(request):
    return render(request,"home_page.html")

def recipe_view(request,pk):
    recipe=get_object_or_404(RecipeStore,id = pk)
    index_obj = get_object_or_404(RecipeIndex, id__id = pk)
    context = {'ing':recipe.ingredients.strip('[]').split(','),'pre':recipe.preparation.strip('[]').split('.'),'img':index_obj.img_url,'desc':recipe.desc,'name':index_obj.recipe_name}
    return render(request, "recipe_view.html",context) 


scrape_progress = { "hebbars_kitchen":threading.Thread(target=hk.scrape_all, name="Hebbars kitchen"),
                    "times_of_india":threading.Thread(target=ti.scrape_all, name="times_of_india"),
                    "yum_recipe":threading.Thread(target=yr.scrape_all, name="yum_recipe")
                    }


def sync(request):
    syncing = False
    if(not scrape_progress.get("hebbars_kitchen").is_alive()):
        syncing = True
        try:
            scrape_progress["hebbars_kitchen"].start()
        except RuntimeError:
            scrape_progress["hebbars_kitchen"] = threading.Thread(target=hk.scrape_all, name="Hebbars kitchen",daemon=True)
            scrape_progress["hebbars_kitchen"].start()
    if(not scrape_progress.get("times_of_india").is_alive()):
        syncing = True
        try:
            scrape_progress["times_of_india"].start()
        except RuntimeError:
            scrape_progress["times_of_india"] = threading.Thread(target=ti.scrape_all, name="times_of_india",daemon=True)
            scrape_progress["times_of_india"].start()
    if(not scrape_progress.get("yum_recipe").is_alive()):
        syncing = True
        try:
            scrape_progress["yum_recipe"].start()
        except RuntimeError:
            scrape_progress["yum_recipe"] = threading.Thread(target=yr.scrape_all, name="yum_recipe",daemon=True)
            scrape_progress["yum_recipe"].start()   
    if(syncing):
        return HttpResponse("Syncing started ..!!!!!")
    else:
        return HttpResponse("Sync already in progress")