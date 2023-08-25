 ```python3
from django.urls import path
from .import views 
 ```

###### 
 ```python3
from django.urls import path
 ```
###### 
 ```python3
from .import views 
 ```

 ```python3
urlpatterns=[
    path('', views.index, name='dashboard-index'),
    path('predictions/', views.predictions, name='dashboard-predictions' )
]
 ```

###### In Django, the urlpatterns list is used to define the URL patterns for your application. These patterns determine how the URLs are matched and which view functions or classes should be executed when a specific URL is accessed. 
 ```python3
urlpatterns=[ ]
 ```

###### 1) path(''): The first argument of the path function is the URL pattern to match. In this case, the empty string '' represents the root path of your application (i.e., the main homepage).

###### 2) views.index: The second argument is the view function or class that should be executed when this URL pattern is accessed. In this case, views.index refers to the index view function defined in the views module.

###### 3) name='dashboard-index': The name parameter assigns a name to this URL pattern. Naming URL patterns is useful for reverse URL matching, where you can refer to URLs by their names instead of their actual paths. In this case, the name 'dashboard-index' is assigned to this URL pattern.
 ```python3
    path('', views.index, name='dashboard-index'),
 ```

###### 1) path('predictions/'): The first argument of the path function is the URL pattern to match. In this case, 'predictions/' represents the path that follows the base URL of your application. When a user accesses this path (e.g., http://yourdomain.com/predictions/), the associated view function or class will be executed.

###### 2) views.predictions: The second argument is the view function or class that should be executed when this URL pattern is accessed. In this case, views.predictions refers to the predictions view function defined in the views module.

###### 3) name='dashboard-predictions': The name parameter assigns a name to this URL pattern. This name is used for reverse URL matching, allowing you to refer to URLs by their names rather than their actual paths. In this case, the name 'dashboard-predictions' is assigned to this URL pattern.
 ```python3
    path('predictions/', views.predictions, name='dashboard-predictions' )
 ```
