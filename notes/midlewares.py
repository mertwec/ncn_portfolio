from ncn.components.quotes import random_quote
from ncn.settings import DATABASES_QUOTER
from notes.models import Category


def categories_sites(request):
    return {"categories": Category.objects.all()}


def quotes_random(request):
    path_to_json = DATABASES_QUOTER
    return {'random_quote': random_quote(path_to_json)}
