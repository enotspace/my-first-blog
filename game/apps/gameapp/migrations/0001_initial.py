# Generated by Django 4.1.4 on 2022-12-10 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=100, verbose_name='Назва гри')),
                ('game_description', models.TextField(verbose_name='Опис гри')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публікації на сайті')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name="Ім'я автора")),
                ('Comment_text', models.TextField(verbose_name='Текст коментаря')),
                ('gameapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapp.game')),
            ],
        ),
    ]
