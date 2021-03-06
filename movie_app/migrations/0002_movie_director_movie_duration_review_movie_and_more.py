# Generated by Django 4.0.5 on 2022-06-25 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.movie'),
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
