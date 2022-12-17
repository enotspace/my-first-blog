# Generated by Django 4.1.4 on 2022-12-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коментар', 'verbose_name_plural': 'Коментарі'},
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Гра', 'verbose_name_plural': 'Ігри'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Comment_text',
            new_name='comment_text',
        ),
        migrations.AddField(
            model_name='game',
            name='game_code',
            field=models.TextField(default=2, verbose_name='Код гри тре вставити в IDE'),
            preserve_default=False,
        ),
    ]
