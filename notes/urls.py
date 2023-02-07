from django.urls import path
from notes.views import notes, delete_note, sites_all, sites_by_category, delete_site

urlpatterns = [
    path('', notes),
    path("delete/<int:note_id>", delete_note),
    path("sites/", sites_all), 
    path("sites/<str:category_name>", sites_by_category, name="site_category"),
    path("sites/delete/<int:site_id>", delete_site)
    ]
