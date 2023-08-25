 ```python3
from django.contrib import admin
from .models import Data
 ```
 ```python3
from django.contrib import admin
 ```

 ```python3
from .models import Data
 ```

# Register your models here.
 ```python3
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time', 'predictions')
admin.site.register(Data, DataAdmin)
 ```

###### 
 ```python3
class DataAdmin(admin.ModelAdmin):
 ```
###### 
 ```python3
    list_display = ('name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time', 'predictions')
 ```
###### 
 ```python3
admin.site.register(Data, DataAdmin)
 ```
