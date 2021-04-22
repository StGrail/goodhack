from django.db import models


class ExhibitionApplication(models.Model):
    ORGANIZER = [
        ('Лично', 'Вы лично (активист)'),
        ('Волонтерское движение', 'Волонтерское движение'),
        ('НКО', 'НКО'),
        ('Образовательное учреждение', 'Образовательное учреждение'),
        ('Молодежная организация', 'Молодежная организация'),
        ('Администрация города/района', 'Администрация города/района')
    ]
    """ Нужно добавить строку с 'другое' с возможностью ввода своего варианта. """

    name = models.CharField(verbose_name='Имя', max_length=25)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    contacts = models.CharField(verbose_name='ВК или email', max_length=100)
    who_is_organize = models.CharField(verbose_name='Кто будет организатором выстаки?',
                                       max_length=100,
                                       choices=ORGANIZER,
                                       default='Лично')
    exhibition_date = models.DateField(verbose_name='Когда примерно хотите организовывать выставку?')
    exhibition_place = models.CharField(verbose_name='Где хотите провести выставку?', max_length=100)
    completed = models.BooleanField(verbose_name='Проведена ли выставка?', default=False)

    def __str__(self):
        return f'{self.name} {self.surname}, контакты - {self.completed}, город - {self.city}, ' \
               f'дата - {self.exhibition_date}, место - {self.exhibition_place}'


class QuizzesForStudentsApplication(models.Model):
    ORGANIZER = [
        ('Лично', 'Вы лично (активист)'),
        ('Волонтерское движение', 'Волонтерское движение'),
        ('НКО', 'НКО'),
        ('Образовательное учреждение', 'Образовательное учреждение'),
        ('Молодежная организация', 'Молодежная организация'),
        ('Администрация города/района', 'Администрация города/района'),
    ]
    """ Нужно добавить строку с 'другое' с возможностью ввода своего варианта. """

    QUIZ_TYPES = [
        ('Малая', 'Малая викторина 45 мин. на класс'),
        ('Большая', 'Большая викторина 1,5 ч. на 50-100 детей'),
        ('Оба варианта', 'Оба варианта'),
    ]

    name = models.CharField(verbose_name='Имя', max_length=25)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    contacts = models.CharField(verbose_name='ВК или email', max_length=100)
    who_is_organize = models.CharField(verbose_name='Кто будет организатором выстаки?',
                                       max_length=100,
                                       choices=ORGANIZER,
                                       default='Лично')
    quiz_format = models.CharField(verbose_name='Какой формат викторин интересует?',
                                   max_length=50,
                                   choices=QUIZ_TYPES,
                                   default='Малая')
    exhibition_date = models.DateField(verbose_name='Когда примерно хотите организовывать выставку?')
    exhibition_place = models.CharField(verbose_name='Где хотите провести выставку?', max_length=100)
    completed = models.BooleanField(verbose_name='Проведена ли ворина?', default=False)

    def __str__(self):
        return f'{self.name} {self.surname}, контакты - {self.completed}, город - {self.city}, ' \
               f'дата - {self.exhibition_date}, место - {self.exhibition_place}'
