# Generated by Django 4.2.7 on 2023-12-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_remove_watchlist_avg_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
