# Generated by Django 2.2.6 on 2019-10-22 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_user',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
