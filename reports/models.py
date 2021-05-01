from django.db import models


class Report(models.Model):
    STATUS = (
        ("Черновик", "Черновик"),
        ("Опубликовано", "Опубликовано")
    )
    TITLE = (
        ("Выставка", "Выставка"),
        ("Викторина", "Викторина")
    )

    title = models.CharField(verbose_name='Название', max_length=200, unique=True)
    content = models.TextField(verbose_name='Текст')
    created_on = models.DateTimeField(auto_now_add=True)
    type = models.CharField(verbose_name='Тип', max_length=100, choices=TITLE)
    status = models.CharField(verbose_name='Статус', max_length=100, choices=STATUS)

    class Meta:
        verbose_name_plural = 'отчеты о проведении выставок/викторин'
        verbose_name = 'отчет о проведении выставок/викторин'
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} - {self.type} - {self.status}'


class ReportImage(models.Model):
    report = models.ForeignKey(Report, default=None, on_delete=models.CASCADE)
    images = models.FileField(verbose_name='фото', blank=True, null=True, upload_to='images/reports/')

    class Meta:
        verbose_name_plural = 'фотографии к отчетам'
        verbose_name = 'фотография'

    def post(self):
        print('Save')
