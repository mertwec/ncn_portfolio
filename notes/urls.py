from django.urls import path
import notes.views as vn

urlpatterns = [
    path('', vn.notes),
    path("delete/<int:note_id>", vn.delete_note),
    path("sites/", vn.sites_all), 
    path("sites/<str:category_name>", vn.sites_by_category, name="site_category"),
    path("sites/delete/<int:site_id>", vn.delete_site),
    ]
