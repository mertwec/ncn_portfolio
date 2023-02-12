from django.db import models, connection
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
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"
        ordering = ["name",]

    def __str__(self):
        return f"{self.name}"


class SiteNote(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(unique=True, null=False)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="sites",
        )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        # verbose_name = "Ссылки"
        db_table = "sites_notes"
        ordering = ["created_at", "title", "url"]

    def __str__(self):
        return f"{self.title}: {self.url}"

    @classmethod
    def get_by_category(cls, category_name):
        query = """
            SELECT 
                sn.id as id, 
                sn.title as title, 
                sn.url as url,
                sn.description as description,
                sn.created_at as created_at
            FROM sites_notes as sn
            JOIN categories as c 
            ON sn.category_id = c.id
            WHERE c.name = %s
            ORDER BY sn.title
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [category_name])
            rows = cursor.fetchall() 
        return [{'id':row[0], 'title':row[1], 'url':row[2]} for row in rows]
        