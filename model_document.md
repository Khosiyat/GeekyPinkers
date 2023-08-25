 ```python3
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
import joblib
 ```
 ```python3
from django.db import models
 ```

 ```python3
from django.core.validators import MaxValueValidator, MinValueValidator 
 ```

 ```python3
import joblib
 ```
CHOICES
------
We can define choices for a field in a Django model using a tuple of tuples. This is typically done when we want to create a field with predefined options. In the following example, each option is represented by a value and a human-readable label and it is defined outside of the model class. We can define the choices within a Django model or outside of the model class itself. This can help keep our code organized, especially if we plan to reuse the same set of choices in multiple places. It is also possible to define the choices in a separate module and then import them where needed.
Let's define 3 choices for three fields: 1Worked_fields 2)Academic_fields 3)Worked_industry
 
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

MODELS
------
 ```python3
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
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


 ```python3
#defining a Django model (Object-Relational Mapping/ORM) class named Data by subclassing models.Model

class Data(models.Model):
 ```

 ```python3
# 1) name: This is the name of the field. You can replace it with any name that makes sense for your model's attributes.

# 2) models.CharField: This indicates that you're using a CharField, which is a field type provided by the models module. CharField is used to store character (string) data.

# 3) max_length=100: This specifies the maximum length of the field in characters. The value 100 in this case means that the field can store up to 100 characters.

# 4) null=True: This option allows the field to be nullable, meaning it can contain a NULL value in the database. By default, Django's CharField doesn't allow NULL values, so specifying null=True makes it optional.

    name = models.CharField(max_length=100, null=True)
 ```

 ```python3
# 1) worked_fields: This is the name of the field you're defining. You can replace it with a name that is meaningful for your model.

# 2) models.PositiveIntegerField: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

# 3) choices=Worked_fields: This specifies the choices that the field can take. Worked_fields should be a sequence of tuples, where each tuple represents a choice consisting of a value and a human-readable label. These choices define the valid options that can be selected for this field.

# 4) null=True: This option allows the field to be nullable, meaning it can contain a NULL value in the database. In this case, setting null=True means the field is optional and can be left empty.

    worked_fields = models.PositiveIntegerField(choices=Worked_fields, null=True)
 ```

 ```python3
# 1) academic_fields: This is the name of the field you're defining. You can replace it with a name that is relevant to your model.

# 2) models.PositiveIntegerField: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

# 3) choices=Academic_fields: This specifies the choices for the field. Academic_fields should be a sequence of tuples, where each tuple represents a choice consisting of a value and a human-readable label. These choices define the valid options that can be selected for this field.

# 4) null=True: This option allows the field to be nullable, meaning it can contain a NULL value in the database. Setting null=True makes the field optional.

    academic_fields = models.PositiveIntegerField(choices=Academic_fields, null=True)
 ```

 ```python3
# 1) worked_industry: This is the name of the field you're defining. You can replace it with a name that makes sense for your model.

# 2) models.PositiveIntegerField: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

# 3) choices=Worked_industry: This specifies the choices for the field. Worked_industry should be a sequence of tuples, where each tuple represents a choice consisting of a value and a human-readable label. These choices define the valid options that can be selected for this field.

# 4) null=True: This option allows the field to be nullable, meaning it can contain a NULL value in the database. Setting null=True makes the field optional.

    worked_industry = models.PositiveIntegerField(choices=Worked_industry, null=True)
 ```

 ```python3
# 1) invested_time: This is the name of the field you're defining. You can replace it with a name that's meaningful for your model.

# 2) models.PositiveIntegerField: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

# 3) validators=[MinValueValidator(1), MaxValueValidator(20)]: This specifies validators for the field. Validators are used to enforce certain constraints on the field's values. In this case, you're using MinValueValidator to ensure that the value is greater than or equal to 1, and MaxValueValidator to ensure that the value is less than or equal to 20.

# 4) null=True: This option allows the field to be nullable, meaning it can contain a NULL value in the database. Setting null=True makes the field optional.

    invested_time = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], null=True)
 ```

 ```python3
# 1) predictions: This is the name of the field you're defining. You can replace it with a name that makes sense for your model.

# 2) models.CharField: This indicates that you're using a CharField, which is a field type provided by the models module. CharField is used to store character (string) data.

# 3) max_length=100: This specifies the maximum length of the field in characters. The value 100 in this case means that the field can store up to 100 characters.

# 4) blank=True: This option allows the field to be left blank when saving data. If blank is set to True, the field will be optional and can have an empty value

    predictions = models.CharField(max_length=100, blank=True)
 ```

 ```python3
# 1) date: This is the name of the field you're defining. You can replace it with a name that's relevant to your model.

# 2) models.DateTimeField: This indicates that you're using a DateTimeField, which is a field type provided by the models module. DateTimeField is used to store date and time information.

# 3) auto_now_add=True: This option automatically sets the field's value to the current date and time when a new record (instance) of the model is created. It's commonly used for fields that represent a creation timestamp

    date = models.DateTimeField(auto_now_add=True)
 ```

 ```python3
    def save(self, *args, **kwargs):
 ```

 ```python3
        ml_model = joblib.load('ml_model/geekyPinkers_model.joblib')
 ```

 ```python3
        self.predictions = ml_model.predict(
            [[ self.worked_industry, self.academic_fields, self.invested_time, self.worked_fields]])
 ```

 ```python3
        return super().save(*args, *kwargs)
 ```

 ```python3
    class Meta:
 ```

 ```python3
        ordering = ['-date']
 ```

 ```python3
    def __str__(self):
 ```

 ```python3
        return self.name
 ```
