# Generated by Django 4.0.5 on 2022-06-30 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_rename_directory_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='directory',
            new_name='directory1',
        ),
    ]
