from django.db import models
from datetime import date

class TestTable (models.Model):
    class Meta:
        verbose_name = 'Тестовая таблица'
        verbose_name_plural = 'Тестовая таблица'

    date_field = models.DateField (
        verbose_name='Дата', blank=False, 
        null=False, default=date.today())
    name = models.CharField (
        verbose_name='Название', max_length=200,
        null=False, blank=False)
    number = models.PositiveIntegerField (verbose_name='Количество',
        null=False, blank=False)
    distance = models.PositiveIntegerField (verbose_name='Расстояние',
        null=False, blank=False)
    visible = models.BooleanField (null=False, blank=False)

    display_number = 0
    page_number = 1

    def __str__(self):
        return f'{self.name}'
    
    def rec_num(self):
        self.display_number = self.objects.all().count()
        return self.display_number
