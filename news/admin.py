from django.contrib import admin

from news.models import News, SourceNews

# Register your models here.

admin.site.register(SourceNews)
# admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', "added_at", "source"]
    list_filter = ['title', "added_at"]
    search_fields = ['title']
    raw_id_fields = ['source']
    ordering = ["added_at"]