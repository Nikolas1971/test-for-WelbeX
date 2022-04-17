from django.contrib import admin
from .models import TestTable

class TestTableDisplay(admin.ModelAdmin):
    list_display = ('date_field', 'name', 'number', 'distance')

admin.site.register (TestTable, TestTableDisplay)
