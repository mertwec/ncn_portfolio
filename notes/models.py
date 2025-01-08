from datetime import datetime

from django.db import connection, models


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
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"
        ordering = ["name", ]

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_names_categories(cls):
        return [cat.name for cat in cls.objects.all()]


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
        return [
            {
                'id': row[0],
                'title': row[1],
                'url': row[2],
                'description': row[3],
                "created_at": row[4]
            } for row in rows
        ]

    @classmethod
    def get_sites(cls):
        query = """
            SELECT sn.title, sn.url, sn.description, 
                c.id, c.name, sn.id
            FROM sites_notes as sn
            JOIN categories as c 
            ON sn.category_id = c.id
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        return [
            {
                "id": i[5],
                'title': i[0],
                'url': i[1],
                'description': i[2],
                'cat_id': i[3],
                'cat_name': i[4]
            } for i in rows
        ]
