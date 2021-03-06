# Generated by Django 3.2 on 2021-04-24 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('contacts', models.CharField(max_length=100, verbose_name='Контакты')),
                ('who_is_organize', models.CharField(choices=[('Активист', 'Вы лично (активист)'), ('Волонтерское движение', 'Волонтерское движение'), ('НКО', 'НКО'), ('Образовательное учреждение', 'Образовательное учреждение'), ('Молодежная организация', 'Молодежная организация'), ('Администрация города/района', 'Администрация города/района')], default='Активист', max_length=100, verbose_name='Организатор мероприятия')),
                ('place', models.CharField(max_length=100, verbose_name='Место проведения мероприятия?')),
                ('date', models.DateField(verbose_name='Примерная дата мероприятие?')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи заявки')),
                ('notes', models.TextField(blank=True, verbose_name='Дополнительная информация от заявителя')),
                ('completed', models.BooleanField(default=False, verbose_name='Проведено ли мероприятие?')),
                ('event_date', models.DateField(blank=True, verbose_name='Дата проведения мероприятия')),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitionApplication',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='application_forms.event')),
                ('visitors_number', models.PositiveIntegerField(blank=True, verbose_name='Количество посетителей')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='Группа/встреча выставки')),
                ('additional_info', models.TextField(blank=True, verbose_name='Примечания')),
            ],
            options={
                'verbose_name': 'заявку на проведение выставки',
                'verbose_name_plural': 'заявки на проведение выставок',
            },
            bases=('application_forms.event',),
        ),
        migrations.CreateModel(
            name='QuizzesForStudentsApplication',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='application_forms.event')),
                ('quiz_format', models.CharField(choices=[('Малая викторина 45 мин. на класс', 'Малая викторина 45 мин. на класс'), ('Большая викторина 1,5 ч. на 50-100 детей', 'Большая викторина 1,5 ч. на 50-100 детей'), ('Оба варианта', 'Оба варианта')], default='Малая викторина 45 мин. на класс', max_length=50, verbose_name='Формат викторины')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='Ссылки на фото/видео/отчеты')),
                ('visitors_number', models.PositiveIntegerField(blank=True, verbose_name='Количество участвующих детей')),
            ],
            options={
                'verbose_name': 'заявку на проведение викторины для школьников',
                'verbose_name_plural': 'заявки на проведение викторин для школьников',
            },
            bases=('application_forms.event',),
        ),
    ]
