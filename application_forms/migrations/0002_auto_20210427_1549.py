# Generated by Django 3.2 on 2021-04-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitionapplication',
            name='visitors_number',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество посетителей'),
        ),
        migrations.AlterField(
            model_name='quizzesforstudentsapplication',
            name='visitors_number',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество участвующих детей'),
        ),
    ]
