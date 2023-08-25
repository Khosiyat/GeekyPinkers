
**[Watch Video about this Forms & Views](https://youtu.be/zcGjaVg9iHk?si=otKmMDNqU6xGeCop)** 
 ```python3
from django import forms
from .models import Data
 ```

 ```python3
from django import forms
 ```

 ```python3
from .models import Data
 ```


 ```python3
class DataForm(forms.ModelForm):
    class Meta:
        model=Data
        fields=['name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time']
```

###### 
 ```python3
class DataForm(forms.ModelForm):
```
###### 
 ```python3
    class Meta:
```
###### 
 ```python3
        model=Data
```
###### 
 ```python3
        fields=['name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time']
```
