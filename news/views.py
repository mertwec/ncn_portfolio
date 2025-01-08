from datetime import datetime, timedelta

from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators import cache, http

from ncn.components.tools_view import paginate_object
from news.models import News, SourceNews
from news.scraping.tools.scraping_tesmanian import (ROOT_URL,
                                                    get_news_tasmania,
                                                    parsing_request)
from news.scraping.tools.tool_requests import get_request


@cache.never_cache
@http.require_http_methods(["GET", "POST"])
def get_news(request: HttpRequest):
    news = News.objects.all()
    ppage = paginate_object(request, news, 6)
    return render(request,
                  template_name="news/news_list.html",
                  context={"news": ppage['objects_on_page'],
                           'page': ppage['page'],
                           "title": "News"})


@http.require_safe
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
                title=info.title,
                url=info.url,
                image_url=info.img.source,
                text=info.text,
                source=source_news[0]
            )

    return redirect(reverse("news:list_news"))

@cache.never_cache
def delete_old_news(request: HttpRequest, N_days: int = 15):
    """ Deleting news from Db if data news > today on N days
    """
    data_ago = datetime.now() - timedelta(days=N_days)
    news = News.objects.all()
    trash_news = news.filter(added_at__lte=data_ago)
    if trash_news:
        trash_news.delete()
        ppage = paginate_object(request, news, 6)

        return render(
            request,
            template_name="news/news_list.html",
            context={
                    "news": ppage['objects_on_page'],
                    'page': ppage['page'],
                    "title": "News",
                    "error_message": f"All News older than {N_days} days is deleted"
                    }
        )
    return redirect(reverse("news:list_news"))