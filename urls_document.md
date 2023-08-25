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
