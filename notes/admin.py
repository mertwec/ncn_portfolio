from django.contrib import admin

from .models import Category, Note, SiteNote

admin.site.register(Note)
admin.site.register(SiteNote)
admin.site.register(Category)
