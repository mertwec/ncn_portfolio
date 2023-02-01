from django.db import models
from datetime import datetime


class Note(models.Model):
    text_content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        # verbose_name = "Заметки"
        db_table = "notes"
        ordering = ["created"]
    
    def __str__(self):
        return f"{self.pk}: {self.text_content}"


class Category(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        # verbose_name = "Category"
        db_table = "categories"
        ordering = "name",

    def __str__(self):
        return f"category: {self.name}"


class SiteNote(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(unique=True, null=False)
    description = models.TextField()
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="sites"
        )

    class Meta:
        # verbose_name = "Ссылки"
        db_table = "sites_notes"
        ordering = ["title", "url"]

    def __str__(self):
        return f"{self.title}: {self.url}"