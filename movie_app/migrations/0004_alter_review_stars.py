# Generated by Django 4.0.5 on 2022-06-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_review_stars_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '*'), (2, '* *'), (3, '* * *'), (4, '* * * *'), (5, '* * * * *')], default=1, null=True),
        ),
    ]
