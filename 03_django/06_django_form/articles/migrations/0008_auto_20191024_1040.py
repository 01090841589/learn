# Generated by Django 2.2.6 on 2019-10-24 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20191024_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='contnet',
            new_name='content',
        ),
    ]
