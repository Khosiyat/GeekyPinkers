 ```python3
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
import joblib
 ```

 ```python3
Worked_fields = (
          (0, 'Worked_fields'), 
          (1, 'Game_development'), 
          (2, 'Software_Developer'), 
          (3, 'Data_science'), 
          (4, 'Mobile_app_development'), 
          (5, 'Data_analysis'), 
          (6, 'Front_end_web_development'), 
          (7, 'Back_end_web_development'), 
          (8, 'Web_design'), 
          (9, 'Machine_learning'), 
          (10, 'Cloud_computing'), 
          (11, 'User_experience_design'), 
          (12, 'Software_Architect'), 
          (13, 'Computer_network'), 
          (14, 'Network_administrator'), 
          (15, 'User_interface_design'), 
          (16, 'Information_technology_management')
          )
```

 ```python3
Academic_fields = (
                   (0, 'None'), 
                   (1, 'Math'), 
                   (2, 'biology'), 
                   (3, 'chemistry'), 
                   (4, 'art'), 
                   (5, 'physics'), 
                   (6, 'History'), 
                   (7, 'literature'), 
                   (8, 'Business'), 
                   (9, 'Social_Sciences'), 
                   (10, 'Psychology'), 
                   (11, 'Communication'), 
                   (12, 'CS'), 
                   (13, 'linguistics')
                   )
 ```

 ```python3
Worked_industry = (
                   (0, 'None'), 
                   (1, 'Transport'), 
                   (2, 'Electronics'), 
                   (3, 'Agriculture'), 
                   (4, 'Food'), 
                   (5, 'Pharmaceutical'), 
                   (6, 'Education'), 
                   (7, 'Energy'),
                    (8, 'Media'), 
                   ( 9, 'Healthcare'), 
                    (10, 'Computer'), 
                   (11, 'Entertainment'), 
                   (12, 'Construction'), 
                   (13,'Telecommunication'), 
                   (14, 'Manufacturing'), 
                   (15, 'Music'), 
                   (16, 'Aerospace'), 
                   (17, 'Entertainment'), 
                   (18, 'Mining'), 
                   (19, 'Hospitality')
                   )
 ```
 ```python3
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    # age = models.PositiveIntegerField(
    # height = models.PositiveIntegerField(null=True)
    # sex = models.PositiveIntegerField(choices=GENDER, null=True)
    worked_fields = models.PositiveIntegerField(choices=Worked_fields, null=True)
    academic_fields = models.PositiveIntegerField(choices=Academic_fields, null=True)
    worked_industry = models.PositiveIntegerField(choices=Worked_industry, null=True)
    invested_time = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/geekyPinkers_model.joblib')
        self.predictions = ml_model.predict(
            [[ self.worked_industry, self.academic_fields, self.invested_time, self.worked_fields]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
 ```
