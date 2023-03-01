from django.urls import path
import notes.views as vn

app_name = 'notes'

urlpatterns = [
    path('', vn.notes),
    path("delete/<int:note_id>", vn.delete_note),

    path("sites/", vn.sites_all),
    path("sites/<str:category_name>", vn.sites_all, name="site_category"), 
    # path("sites/delete/<int:site_id>", vn.delete_site),
    path("sites/dump/", vn.dump_sites_db, name='sites_dump'),
    path("sites/load_dump/", vn.load_dump_sites_db, name="sites_load"),
    ]
