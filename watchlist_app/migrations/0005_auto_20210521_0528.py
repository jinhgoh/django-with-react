# Generated by Django 3.2.3 on 2021-05-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_imagetest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetest',
            name='img',
        ),
        migrations.AddField(
            model_name='imagetest',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]