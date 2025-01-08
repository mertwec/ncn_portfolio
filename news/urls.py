from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [
    path('', views.get_news, name="list_news"),
    path("update/", views.update_news, name="get_latest_news"),
    path("delete/", views.delete_old_news, name="delete_old_news")

    # path("sites/<str:category_name>", vn.sites_all, name="site_category"), 
    ]
