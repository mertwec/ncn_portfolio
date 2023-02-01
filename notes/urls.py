from django.urls import path
from notes.views import notes, note_delete

urlpatterns = [
    path('', notes),
    # path("add/", note_add),
    path("delete/<int:note_id>", note_delete)
    ]
