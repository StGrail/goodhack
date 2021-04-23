from django.contrib import admin

from .models import QuizzesForStudentsApplication, ExhibitionApplication


class BaseApplicationFormAdmin(admin.ModelAdmin):
    """
    Базовый класс для заявок на выставки и школьные викторины.
    Включает в себя полностью рабочий класс для выставки.
    """
    fieldsets = (
        ('Данные заявителя', {
            'fields': ('name', 'surname', 'city', 'contacts', 'registration_date')
        }),
        ('Данные о выставке', {
            'fields': ('who_is_organize', 'date', 'place'),
        }),
        ('Поставьте галочку, если провели мероприятие', {
            'fields': ('completed',),
        })
    )
    list_display = (
        'name', 'surname', 'city', 'contacts', 'who_is_organize', 'place', 'date', 'registration_date', 'completed')
    list_filter = ['completed', 'registration_date']
    ordering = ['-registration_date']


@admin.register(ExhibitionApplication)
class ExhibitionAdmin(BaseApplicationFormAdmin):
    pass


@admin.register(QuizzesForStudentsApplication)
class QuizzesAdmin(BaseApplicationFormAdmin):
    fieldsets = (
        ('Данные заявителя', {
            'fields': ('name', 'surname', 'city', 'contacts', 'registration_date')
        }),
        ('Данные о выставке', {
            'fields': ('who_is_organize', 'quiz_format', 'date', 'place'),
        }),
        ('Поставьте галочку, если провели мероприятие', {
            'fields': ('completed',),
        })
    )
