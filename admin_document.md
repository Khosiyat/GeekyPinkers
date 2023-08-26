 ```python3
from django.contrib import admin
from .models import Data
 ```

###### Let's bring the `admin` module from the django.contrib package into our current Python script or module. The contrib module contains various "contributed" modules and packages that provide additional functionality and features to Django projects. These modules are not part of the core Django framework but are commonly used and maintained by the community. The `admin` module is a core part of Django's administration interface, which allows us to easily manage our application's data through a web-based user interface. When we import the admin module, we gain access to classes and functionality that help us define and customize the administration interface for our Django models. This interface allows us to create, update, and delete records in our database tables without writing custom views or templates.

 ```python3
from django.contrib import admin
 ```
###### Now we may bring the Data class from a module named models in the same package or directory as our current Python script or module.

###### `from .models`: This part indicates that we're importing something from a module named models that is located in the same package or directory as our current script. The dot . represents the current package or directory.

###### `import` Data: This part specifies that we want to import the `Data` class from the models module.

###### In Django, the models module is typically used to define our application's data models using Django's Object-Relational Mapping (ORM) system. A model represents a database table and its fields as a Python class. The `Data` class we're importing likely corresponds to a model class that we've defined in our Django application.

###### So, when we import `Data` using `from .models import Data`, we're bringing this `Data` model class into our current script, which allows us to work with it, query the database, create new records, retrieve data, and perform various operations related to database interactions using this class.

 ```python3
from .models import Data
 ```

# Register your models here.
 ```python3
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time', 'predictions')
admin.site.register(Data, DataAdmin)
 ```

###### Let's define a Django `admin` class named `DataAdmin` by subclassing `admin.ModelAdmin`.

 ```python3
class DataAdmin(admin.ModelAdmin):
 ```
###### In our case we are defining a Django `admin` class using `list_display` to customize `DataAdmin` class.
###### We can further customize the `DataAdmin` class by adding more attributes and methods as needed based on how we want to present and manage our data in the `admin` interface.
###### Keep in mind that the specific attributes and methods we need to define in `DataAdmin` will depend on the fields and behavior of our Data model and how we want to interact with it in the `admin` interface.

###### - `list_display`: Specifies the fields that will be displayed in the list view of the admin interface for the Data model.
###### - `list_filter`: Adds a filter option in the right sidebar of the admin list view, allowing us to filter data based on the selected field.
###### - `search_fields`: Enables a search bar in the admin interface, allowing us to search for data based on the specified fields.
###### - `admin.site.register(Data, DataAdmin)`: Registers the Data model with the DataAdmin class, linking our custom admin configuration to the model.


 ```python3
    list_display = ('name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time', 'predictions')
 ```
###### Let's register the Data model with the DataAdmin class we defined by using the `admin.site.register(Data, DataAdmin)` line. This line is a crucial step in connecting our custom admin configuration with the specific model, allowing us to manage and display instances of the Data model using the customized admin interface defined in the DataAdmin class.

###### `admin.site`: This refers to the global instance of the Django admin site. We access this instance to register models and configure their corresponding admin classes.

###### `register(Data, DataAdmin)`: The register method of the admin site is used to associate a model with its corresponding admin class. In our case, we're associating the `Data` model with the `DataAdmin` class, meaning that the `admin` interface for the `Data` model will follow the customizations and settings defined in `DataAdmin`.

###### This line essentially tells Django's admin system to use the `DataAdmin` class to manage instances of the Data model within the admin interface. This way, when we access the admin interface for our Django project and navigate to the section related to the Data model, we'll see the customizations and configurations we've defined in the DataAdmin class. This can include how the data is displayed, filtered, searched, and more.

 ```python3
admin.site.register(Data, DataAdmin)
 ```


 
#### **[Watch the tutorial](https://www.youtube.com/playlist?list=PLoRaeB82EdK6ZIdpklyBUj7qWhvbVDCw- )**

1. **[Introduction](https://youtu.be/gWZf-mR1IgM?si=fY_5kUdOUs9xM73N)**
2. **[Machine Learning Model Training](https://youtu.be/QuVoz2bkssQ?si=b-WUsUxmE9KR2sZG)**
3. **[Install Django](https://youtu.be/VWdJOB6hOXU?si=dlXWnc6Jvl0usPsd)**
4. **[Model](https://youtu.be/xtHFkowf55o?si=mYHC5eh7-6wwdhVA)**
5. **[Forms & Views](https://youtu.be/zcGjaVg9iHk?si=otKmMDNqU6xGeCop)**
6. **[Templates](https://youtu.be/MxpcVszpVgc?si=wYy1lsKjOILYT3l0)**

#### **[Documentation (explanation) of the apps of GeekPinkers Project:](https://github.com/Khosiyat/GeekyPinkers/blob/main/README.md)**

1. **[apps.py:](https://github.com/Khosiyat/GeekyPinkers/blob/main/apps_document.md)**
2. **[admin.py:](https://github.com/Khosiyat/GeekyPinkers/blob/main/admin_document.md)**
3. **[model.py:](https://github.com/Khosiyat/GeekyPinkers/blob/main/model_document.md)**
4. **[forms.py:](https://github.com/Khosiyat/GeekyPinkers/blob/main/form_document.md)**
5. **[urls.py:](https://github.com/Khosiyat/GeekyPinkers/blob/main/urls_document.md)**
6. **[views.py:](https://github.com/Khosiyat/GeekyPinkers/blob/main/views_document.md)**
