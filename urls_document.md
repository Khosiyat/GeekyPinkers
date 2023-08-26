 ```python3
from django.urls import path
from .import views 
 ```

###### The line `from django.urls import path` is importing the path function from the `django.urls` module.

###### The `path` function is used to associate a `URL pattern` with a specific `view` function. It's a key part of how Django handles routing and navigation within our application. Here's a simple example of how the path function is typically used in our `urls.py` file:
 
###### These `URL` patterns define how different parts of our web application respond to incoming requests. When a user navigates to a specific `URL`, Django uses the `URL patterns` to determine which view function should be called to handle that request.

 ```python3
from django.urls import path
 ```
###### In this statement, we're importing the `views` module from the same package or directory as the current script. This is a common practice in Django projects, where we define `views` in the `views.py` module and then import them into other parts of our app, such as `URL`s, other `views`, or other modules.

###### Once we've imported the `views` module, we can access the functions or classes defined in that module using the views namespace. For example, we have a view function named `index` defined in the views module:

 ```python3
from .import views 
 ```

 ```python3
urlpatterns=[
    path('', views.index, name='dashboard-index'),
    path('predictions/', views.predictions, name='dashboard-predictions' )
]
 ```

###### In Django, the `urlpatterns` list is used to define the `URL` patterns for our application. These patterns determine how the `URL`s are matched and which view functions or classes should be executed when a specific `URL` is accessed. 
 ```python3
urlpatterns=[ ]
 ```

###### 1) `path('')`: The first argument of the path function is the `URL` pattern to match. In this case, the empty string `''` represents the root `path` of our application (i.e., the main homepage).

###### 2) `views.index`: The second argument is the `view` function or class that should be executed when this `URL` pattern is accessed. In this case, `views.index` refers to the index view function defined in the views module.

###### 3) `name='dashboard-index'`: The name parameter assigns a name to this `URL` pattern. Naming `URL` patterns is useful for reverse `URL` matching, where we can refer to `URL`s by their names instead of their actual `path`s. In this case, the name `'dashboard-index'` is assigned to this `URL` pattern.
 ```python3
    path('', views.index, name='dashboard-index'),
 ```

###### 1) `path('predictions/')`: The first argument of the `path` function is the `URL` pattern to match. In this case, `'predictions/'` represents the `path` that follows the base `URL` of our application. When a user accesses this `path` (e.g., http://yourdomain.com/predictions/), the associated view function or class will be executed.

###### 2) `views.predictions`: The second argument is the view function or class that should be executed when this `URL` pattern is accessed. In this case, `views.predictions` refers to the predictions view function defined in the views module.

###### 3) `name='dashboard-predictions'`: The name parameter assigns a name to this `URL` pattern. This name is used for reverse `URL` matching, allowing us to refer to `URL`s by their names rather than their actual paths. In this case, the name `'dashboard-predictions'` is assigned to this `URL` pattern.
 ```python3
    path('predictions/', views.predictions, name='dashboard-predictions' )
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
