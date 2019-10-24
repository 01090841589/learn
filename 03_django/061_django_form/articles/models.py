from django.db import models
from django.conf import settings

class Hashtag(models.Model):
    content = models.TextField(unique=True)
    def __str__(self):
        return self.content


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    class Meta:
        ordering = ('-pk', )
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=50)
    created_user = models.CharField(max_length=50, default='admin')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-pk', )
    def __str__(self):
        return self.content