from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

def article_image_path(instance, filename):
    return f'articles/{instance.pk}번글/images/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source='image',
    #     processors=[Thunmnail(200,300)],
    #     format='JPEG',
    # )
    image = ProcessedImageField(
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90},
        upload_to=articles_image_path,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    models.IntegerField

    def __str__(self):
        return f'제목: {self.title}, 내용: {self.content}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk', ]
    def __str__(self):
        # return f'댓글: {self.content}'
        return f'<Article({self.article_id}): Comment({self.pk} - {self.content})>'

# Create your models here.
