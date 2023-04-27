from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from django.views.decorators.cache import never_cache
from django.db import transaction

from news.models import SourceNews, News
from news.scraping.tools.scraping_tesmanian import ROOT_URL, parsing_request, get_news_tasmania
from news.scraping.tools.tool_requests import get_request


@never_cache
def get_news(request: HttpRequest):
    news = News.objects.all()
    return render(request, 
                  template_name="news/news_list.html", 
                  context={"news": news, 
                           "title": "News"})


def update_news(request: HttpRequest):
    source_news = SourceNews.objects.get_or_create(title='tesmanian',
                                              site="https://www.tesmanian.com/")
    
    page = get_request(ROOT_URL)
    if isinstance(page, str):
        return render(request, 
                  template_name="news/news_list.html", 
                  context={"news": None, 
                           "title": "News",
                           "error_message": f"Not connect with {ROOT_URL}"})
    soup = parsing_request(page)
    new_news = get_news_tasmania(soup)
    with transaction.atomic():
        for info in new_news:
            News.objects.get_or_create(
                title = info.title,
                url = info.url,
                image_url = info.img.source,
                text = info.text,
                source = source_news[0]          
            )   

    return redirect(reverse("news:list_news"))


def delete_old_news(request: HttpRequest, N_days: int=15):
    """ Deleting news from Db if data news > today on N days
    """
    data_ago = datetime.now() - timedelta(days=N_days)
    trash_news = News.objects.all().filter(added_at__gt=data_ago)
    breakpoint()

    return redirect(reverse("news:list_news"))
