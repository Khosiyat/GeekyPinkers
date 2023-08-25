[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)]([http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE](https://www.youtube.com/watch?v=QuVoz2bkssQ&list=PLoRaeB82EdK6ZIdpklyBUj7qWhvbVDCw-&index=2))

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

###### defining a Django model (Object-Relational Mapping/ORM) class named Data by subclassing models.Model

 ```python3
class Data(models.Model):
 ```


###### 1) `name`: This is the name of the field. You can replace it with any name that makes sense for your model's attributes.

###### 2) `models.CharField`: This indicates that you're using a CharField, which is a field type provided by the models module. CharField is used to store character (string) data.

###### 3) `max_length=100`: This specifies the maximum length of the field in characters. The value 100 in this case means that the field can store up to 100 characters.

###### 4) `null=True`: This option allows the field to be nullable, meaning it can contain a NULL value in the database. By default, Django's CharField doesn't allow NULL values, so specifying null=True makes it optional.

 ```python3
    name = models.CharField(max_length=100, null=True)
 ```

###### 1) `worked_fields`: This is the name of the field you're defining. You can replace it with a name that is meaningful for your model.

###### 2) `models.PositiveIntegerField`: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

###### 3) `choices=Worked_fields`: This specifies the choices that the field can take. Worked_fields should be a sequence of tuples, where each tuple represents a choice consisting of a value and a human-readable label. These choices define the valid options that can be selected for this field.

###### 4) `null=True`: This option allows the field to be nullable, meaning it can contain a NULL value in the database. In this case, setting null=True means the field is optional and can be left empty.

 ```python3
    worked_fields = models.PositiveIntegerField(choices=Worked_fields, null=True)
 ```

###### 1) `academic_fields`: This is the name of the field you're defining. You can replace it with a name that is relevant to your model.

###### 2) `models.PositiveIntegerField`: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

###### 3) `choices=Academic_fields`: This specifies the choices for the field. Academic_fields should be a sequence of tuples, where each tuple represents a choice consisting of a value and a human-readable label. These choices define the valid options that can be selected for this field.

###### 4) `null=True`: This option allows the field to be nullable, meaning it can contain a NULL value in the database. Setting null=True makes the field optional.

 ```python3
    academic_fields = models.PositiveIntegerField(choices=Academic_fields, null=True)
 ```

###### 1) `worked_industry`: This is the name of the field you're defining. You can replace it with a name that makes sense for your model.

###### 2) `models.PositiveIntegerField`: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

###### 3) `choices=Worked_industry`: This specifies the choices for the field. Worked_industry should be a sequence of tuples, where each tuple represents a choice consisting of a value and a human-readable label. These choices define the valid options that can be selected for this field.

###### 4) `null=True`: This option allows the field to be nullable, meaning it can contain a NULL value in the database. Setting null=True makes the field optional.

 ```python3
    worked_industry = models.PositiveIntegerField(choices=Worked_industry, null=True)
 ```

###### 1) `invested_time`: This is the name of the field you're defining. You can replace it with a name that's meaningful for your model.

###### 2) `models.PositiveIntegerField`: This indicates that you're using a PositiveIntegerField, which is a field type provided by the models module. PositiveIntegerField is used to store positive integer values.

###### 3) `validators=[MinValueValidator(1), MaxValueValidator(20)]`: This specifies validators for the field. Validators are used to enforce certain constraints on the field's values. In this case, you're using MinValueValidator to ensure that the value is greater than or equal to 1, and MaxValueValidator to ensure that the value is less than or equal to 20.

###### 4) `null=True`: This option allows the field to be nullable, meaning it can contain a NULL value in the database. Setting null=True makes the field optional.


 ```python3
    invested_time = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], null=True)
 ```

###### 1) `predictions`: This is the name of the field you're defining. You can replace it with a name that makes sense for your model.

###### 2) `models.CharField`: This indicates that you're using a CharField, which is a field type provided by the models module. CharField is used to store character (string) data.

###### 3) `max_length=100`: This specifies the maximum length of the field in characters. The value 100 in this case means that the field can store up to 100 characters.

###### 4) `blank=True`: This option allows the field to be left blank when saving data. If blank is set to True, the field will be optional and can have an empty value


 ```python3
    predictions = models.CharField(max_length=100, blank=True)
 ```

###### 1) `date`: This is the name of the field you're defining. You can replace it with a name that's relevant to your model.

###### 2) `models.DateTimeField`: This indicates that you're using a DateTimeField, which is a field type provided by the models module. DateTimeField is used to store date and time information.

###### 3) `auto_now_add=True`: This option automatically sets the field's value to the current date and time when a new record (instance) of the model is created. It's commonly used for fields that represent a creation timestamp

 ```python3
    date = models.DateTimeField(auto_now_add=True)
 ```

###### This is the custom `save` method within the model. By defining this method, you're providing your own implementation of how the instance should be saved.
###### The `*args` and `**kwargs` are used to pass any arguments and keyword arguments that were passed to the save method.
###### In Python, self is a conventionally used name for the first parameter of instance methods. It refers to the instance of the class that the method is being called on. In the context of a Django model, self refers to the instance of the model that you're currently working with.
 ```python3
    def save(self, *args, **kwargs):
 ```

###### loading a machine learning model from a joblib file named 'geekyPinkers_model.joblib'.
###### 1) ml_model: This is a variable name that you're using to store the loaded machine learning model.
###### 2) joblib.load('ml_model/geekyPinkers_model.joblib'): This is a function call to the load function from the joblib library. The function is used to load a serialized object (in this case, your machine learning model) from a joblib file named 'geekyPinkers_model.joblib'. The file should be located in a directory named 'ml_model'. The loaded model will be assigned to the ml_model variable.

 ```python3
        ml_model = joblib.load('ml_model/geekyPinkers_model.joblib')
 ```

###### using the loaded machine learning model to make predictions based on certain input features. Let's break down what's happening:

###### 1) `self.predictions`: This is setting the predictions attribute of the instance (the object that the method is called on) with the predictions generated by the machine learning model.

###### 2) `ml_model.predict(...)`: This calls the predict method of the loaded machine learning model (ml_model) to generate predictions. The method takes a 2D array-like input containing the feature values for which predictions are to be made.

###### 3) `[[ self.worked_industry, self.academic_fields, self.invested_time, self.worked_fields]]`: This creates a 2D array with a single row, where each column represents the input features needed for making a prediction. The values of self.worked_industry, self.academic_fields, self.invested_time, and self.worked_fields are being used as the input features for prediction

 ```python3
        self.predictions = ml_model.predict(
            [[ self.worked_industry, self.academic_fields, self.invested_time, self.worked_fields]])
 ```
###### 1) `super()`: This is a built-in Python function that returns a temporary object of the superclass, allowing you to call its methods. In this context, super() is used to refer to the parent class of the current class (i.e., the models.Model class).

###### 2) `.save(*args, **kwargs)`: This calls the save method of the parent class (models.Model) and passes any arguments and keyword arguments (*args and **kwargs) that were provided to the current save method.

###### 3) `return`: This returns the result of calling the parent class's save method.

 ```python3
        return super().save(*args, *kwargs)
 ```
###### The class Meta inside a Django model is a nested class used to provide metadata and options for the model. It allows you to configure various aspects of how the model interacts with the database and other behaviors. The Meta class is a powerful way to control how your model interacts with the database and how it's displayed in the Django admin interface. 
 ```python3
    class Meta:
 ```
###### `The line ordering = ['-date']` inside the class `Meta` of a Django model is specifying that querysets retrieved from the database should be ordered in descending order based on the date field. This means that the most recent records will appear first in the queryset.

 ```python3
        ordering = ['-date']
 ```
###### The `def __str__(self)`: method is a special method in a Django model class that defines how instances of the model should be represented as strings. This method is used primarily for human-readable representation, such as in the Django admin interface or when printing instances in Python. In this example, the `__str__` method is overridden in the Data Model class. The method returns the value of the field1 attribute as a string when an instance of the model is converted to a string. This is useful for making the representation more human-friendly, as you can see when you interact with instances in the Django admin or other parts of your code.
 ```python3
    def __str__(self):
 ```
######  When you convert an instance of Data Model to a string, it will return the value of the name field. This can be very helpful for identifying instances in a human-readable format, especially when working with the Django admin interface or when printing instances in your code.
 ```python3
        return self.name
 ```
