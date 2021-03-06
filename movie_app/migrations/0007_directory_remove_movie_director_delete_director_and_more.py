# Generated by Django 4.0.5 on 2022-06-28 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_review_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.AddField(
            model_name='movie',
            name='directory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.directory'),
        ),
    ]
