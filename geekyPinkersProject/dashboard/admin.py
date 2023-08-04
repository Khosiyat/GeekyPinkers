from django.contrib import admin
from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time', 'predictions')


admin.site.register(Data, DataAdmin)