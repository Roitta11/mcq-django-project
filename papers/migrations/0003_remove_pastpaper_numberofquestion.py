# Generated by Django 4.0.2 on 2022-07-17 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_pastpaper_numberofquestion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastpaper',
            name='numberOfQuestion',
        ),
    ]
