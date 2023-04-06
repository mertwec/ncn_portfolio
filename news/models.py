from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=30)

#     class Meta:
#         db_table = "news_category"


class SourceNews(models.Model):
    title = models.CharField(max_length=254, default='news')
    site = models.URLField(null=False, blank=False, unique=True)

    class Meta:
        db_table = "news_sites"
        verbose_name = 'Source news'
        verbose_name_plural = 'Sources news'

    def __str__(self):
        return f"{self.title}: {self.site}"


class News(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    url = models.URLField(null=False, blank=False, unique=True)
    image_url = models.URLField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    source = models.ForeignKey(
        SourceNews,
        on_delete=models.CASCADE,
        related_name='site_news',
        null=False,
        blank=False
    )
    # category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='news')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.title}: {self.url}   {self.added_at}"
