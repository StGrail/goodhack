from django.contrib import admin

from .models import QuizzesForStudentsApplication, ExhibitionApplication


@admin.action(description='Отметить выбранные мероприятия как проведенные')
def make_completed(modeladmin, request, queryset):
    queryset.update(completed=True)


class BaseApplicationFormAdmin(admin.ModelAdmin):
    """
    Базовый класс для заявок на выставки и школьные викторины.
    Включает в себя полностью рабочий класс для выставки.
    """
    fieldsets = (
        ('Данные заявителя', {
            'fields': ('name', 'surname', 'city', 'contacts')
        }),
        ('Данные о выставке', {
            'fields': ('who_is_organize', 'date', 'place', 'notes'),
        }),
        ('Поставьте галочку, если провели мероприятие', {
            'fields': ('completed',),
        }),
        ('Отчет о проведении', {
            'fields': ('visitors_number', 'link', 'additional_info', 'event_date'),
        }),
    )
    list_display = (
        'name', 'surname', 'city', 'contacts', 'who_is_organize', 'place', 'date', 'registration_date', 'completed')
    list_filter = ['completed', 'registration_date']
    ordering = ['-registration_date']
    actions = [make_completed]


@admin.register(ExhibitionApplication)
class ExhibitionAdmin(BaseApplicationFormAdmin):
    pass


@admin.register(QuizzesForStudentsApplication)
class QuizzesAdmin(BaseApplicationFormAdmin):
    fieldsets = (
        ('Данные заявителя', {
            'fields': ('name', 'surname', 'city', 'contacts')
        }),
        ('Данные о викторине', {
            'fields': ('who_is_organize', 'quiz_format', 'date', 'place', 'notes'),
        }),
        ('Поставьте галочку, если провели мероприятие', {
            'fields': ('completed',),
        }),
        ('Отчет о проведении', {
            'fields': ('visitors_number', 'link', 'event_date'),
        }),
    )
