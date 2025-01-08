
from django.core.paginator import Page, Paginator
from django.db.models import QuerySet
from django.http import HttpRequest


def paginate_object(request: HttpRequest,
                    object_list: QuerySet,
                    count_object_on_page: int) -> dict:

    paginator = Paginator(object_list, count_object_on_page)
    if 'page' in request.GET:
        page_num = request.GET["page"]
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    return {'page': page,
            'page_num': page_num,
            'objects_on_page': page.object_list}
