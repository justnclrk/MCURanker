# Generated by Django 3.0.5 on 2020-04-10 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0007_auto_20200409_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rank',
            options={'ordering': ['number']},
        ),
    ]
