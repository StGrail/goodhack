from django.db import models


class Event(models.Model):
    """
    Базовый класс для заявок на выставки и школьные викторины.
    Включает в себя полностью рабочий класс для выставки.
    """

    ORGANIZER = [
        ('Активист', 'Вы лично (активист)'),
        ('Волонтерское движение', 'Волонтерское движение'),
        ('НКО', 'НКО'),
        ('Образовательное учреждение', 'Образовательное учреждение'),
        ('Молодежная организация', 'Молодежная организация'),
        ('Администрация города/района', 'Администрация города/района')
    ]
    name = models.CharField(verbose_name='Имя', max_length=25)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    contacts = models.CharField(verbose_name='Контакты', max_length=100)
    who_is_organize = models.CharField(verbose_name='Организатор мероприятия',
                                       max_length=100,
                                       choices=ORGANIZER,
                                       default='Активист')
    place = models.CharField(verbose_name='Место проведения мероприятия?', max_length=100)
    date = models.DateField(verbose_name='Примерная дата мероприятие?')
    registration_date = models.DateTimeField(verbose_name='Дата подачи заявки', auto_now_add=True)
    notes = models.TextField(verbose_name='Дополнительная информация от заявителя', blank=True)
    completed = models.BooleanField(verbose_name='Проведено ли мероприятие?', default=False)
    event_date = models.DateField(verbose_name='Дата проведения мероприятия', blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}, контакты - {self.contacts}, город - {self.city}, ' \
               f'место проведения - {self.place}, дата проведения - {self.date}'


class ExhibitionApplication(Event):
    visitors_number = models.PositiveIntegerField(verbose_name='Количество посетителей', blank=True, default=0)
    link = models.CharField(verbose_name='Группа/встреча выставки', max_length=255, blank=True)
    additional_info = models.TextField(verbose_name='Примечания', blank=True)

    class Meta:
        verbose_name_plural = 'заявки на проведение выставок'
        verbose_name = 'заявку на проведение выставки'


class QuizzesForStudentsApplication(Event):
    QUIZ_TYPES = [
        ('Малая викторина 45 мин. на класс', 'Малая викторина 45 мин. на класс'),
        ('Большая викторина 1,5 ч. на 50-100 детей', 'Большая викторина 1,5 ч. на 50-100 детей'),
        ('Оба варианта', 'Оба варианта'),
    ]

    quiz_format = models.CharField(verbose_name='Формат викторины',
                                   max_length=50,
                                   choices=QUIZ_TYPES,
                                   default='Малая викторина 45 мин. на класс')
    link = models.CharField(verbose_name='Ссылки на фото/видео/отчеты', max_length=255, blank=True)
    visitors_number = models.PositiveIntegerField(verbose_name='Количество участвующих детей', blank=True, default=0)

    class Meta:
        verbose_name_plural = 'заявки на проведение викторин для школьников'
        verbose_name = 'заявку на проведение викторины для школьников'
