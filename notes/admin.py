from django.contrib import admin
from .models import Note, SiteNote, Category


admin.site.register(Note)
admin.site.register(SiteNote)
admin.site.register(Category)
