from django.db import models


class Event(models.Model):
    """
    Базовый класс для заявок на выставки и школьные викторины.
    Включает в себя полностью рабочий класс для выставки.
    """

    ORGANIZER = [
        ('Лично', 'Вы лично (активист)'),
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
    who_is_organize = models.CharField(verbose_name='Кто будет организатором выставки?',
                                       max_length=100,
                                       choices=ORGANIZER,
                                       default='Лично')
    date = models.DateField(verbose_name='Когда примерно хотите организовывать выставку?')
    place = models.CharField(verbose_name='Где хотите провести выставку?', max_length=100)
    completed = models.BooleanField(verbose_name='Проведена ли выставка?', default=False)

    def __str__(self):
        return f'{self.name} {self.surname}, контакты - {self.contacts}, город - {self.city}, ' \
               f'место проведения - {self.place}, дата проведения - {self.date}'


class ExhibitionApplication(Event):
    class Meta:
        verbose_name_plural = 'Заявки на проведение выставок'
        verbose_name = 'заявку на проведение выставки'


class QuizzesForStudentsApplication(Event):
    QUIZ_TYPES = [
        ('Малая викторина 45 мин. на класс', 'Малая викторина 45 мин. на класс'),
        ('Большая викторина 1,5 ч. на 50-100 детей', 'Большая викторина 1,5 ч. на 50-100 детей'),
        ('Оба варианта', 'Оба варианта'),
    ]

    quiz_format = models.CharField(verbose_name='Какой формат викторин интересует?',
                                   max_length=50,
                                   choices=QUIZ_TYPES,
                                   default='Малая')

    class Meta:
        verbose_name_plural = 'заявки на проведение викторин для школьников'
        verbose_name = 'заявку на проведение викторины для школьников'
