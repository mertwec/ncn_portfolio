from notes.models import Category
from components.quotes import random_quote
from ncn.settings import DATABASES_QUOTER


def categories_sites(request):
    return {"categories": Category.objects.all()}

def quotes_random(request):
    path_to_json = DATABASES_QUOTER
    return {'random_quote': random_quote(path_to_json)
    }
