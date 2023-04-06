from django.urls import path
import notes.views as v_note

app_name = 'notes'

urlpatterns = [
    path('', v_note.notes),
    path("delete/<int:note_id>", v_note.delete_note),

    path("sites/", v_note.sites_all),
    path("sites/<str:category_name>", v_note.sites_all, name="site_category"), 
    # path("sites/delete/<int:site_id>", v_note.delete_site),
    path("sites/dump/", v_note.dump_sites_db, name='sites_dump'),
    path("sites/load_dump/", v_note.load_dump_sites_db, name="sites_load"),
    ]
