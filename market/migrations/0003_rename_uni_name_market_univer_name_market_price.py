# Generated by Django 4.1.2 on 2022-10-29 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_market_views_alter_marketfiledemo_market_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='uni_name',
            new_name='univer_name',
        ),
        migrations.AddField(
            model_name='market',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
