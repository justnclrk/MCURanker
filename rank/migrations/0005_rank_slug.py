# Generated by Django 3.0.5 on 2020-04-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0004_auto_20200407_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
