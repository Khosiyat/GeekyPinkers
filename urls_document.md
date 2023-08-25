 ```python3
from django.urls import path
from .import views 
 ```

 ```python3
urlpatterns=[
    path('', views.index, name='dashboard-index'),
    path('predictions/', views.predictions, name='dashboard-predictions' )
]
 ```


 ```python3
urlpatterns=[ ]
 ```


 ```python3
    path('', views.index, name='dashboard-index'),
 ```


 ```python3
    path('predictions/', views.predictions, name='dashboard-predictions' )
 ```
