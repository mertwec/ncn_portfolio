from notes.models import Category
from components.quotes import random_quote
from ncn.settings import BASE_DIR
import os


def categories_sites(request):
    return {"categories": Category.objects.all()}

def quotes_random(request):
    path_to_json = os.path.join(BASE_DIR, "static", "quotes.json")
    return {'random_quote': random_quote(path_to_json)}