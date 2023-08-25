from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model=Data
        fields=['name', 'worked_fields', 'academic_fields', 'worked_industry', 'invested_time']
