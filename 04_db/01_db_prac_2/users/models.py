from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    balance = models.IntegerField()

    def __str__(self):
        return f'제목: {self.title}, 내용: {self.content}'
