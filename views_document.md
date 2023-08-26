**[Watch video about this Views and Forms](https://youtu.be/zcGjaVg9iHk?si=otKmMDNqU6xGeCop)**
 ```python3
from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
 ```
###### `render(request, template_name, context=None, content_type=None, status=None, using=None)`: This function is used to render an  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**  template with a given context and return an `HttpResponse` object. It's often used to generate dynamic web pages using templates. The request argument is the `HTTP` request object, and template_name is the name of the template to be rendered. We can also provide a `context dictionary `that contains data to be used in the template.

###### `redirect(to, *args, permanent=False, **kwargs)`: This function is used to create a redirect response. It takes a `URL` as the `to` argument and redirects the user to that `URL`. The permanent argument specifies whether the redirect should be permanent (`HTTP` status code `301`) or temporary (`HTTP` status code `302`). We can also pass additional arguments and keyword arguments to customize the redirect behavior.

 ```python3
from django.shortcuts import render, redirect
 ```
###### `from .forms`: The dot `.` indicates the current package or directory. We're importing something from within the same package.
###### `import DataForm`: This imports the `DataForm` class from the `forms.py` module.


 ```python3
from .forms import DataForm
 ```

###### `from .models`: The dot `.` refers to the current package or directory. So, we're importing something from within the same package.
###### `import Data`: This imports the `Data` model from the `models.py` module in the same directory/package.

 ```python3
from .models import Data
 ```

# Create your views here.
 ```python3
def index(request):
    if request.method=="POST":
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')  

    else:
        form = DataForm()

    
    context={
        'form':form
    }

    return render(request, "index.html", context) 
 ```
###### View functions are responsible for handling incoming `HTTP` requests and returning appropriate `HTTP` responses. Here's what each part of this line means:

###### 1) `def`: This is the Python keyword used to define a function.

###### 2) `index`: This is the name of the view function. We can replace `index` with a name that represents the purpose of the `view`.

###### 3) `(request)`: The parameter `(request)` represents the incoming `HTTP` request object. This parameter is automatically passed to the view function by Django when a user accesses the corresponding `URL`.

 ```python3
def index(request):
 ```
###### The condition `if request.method == "POST":` is commonly used in Django view functions to check if the incoming `HTTP` request is a `POST request`. This is often used when we want to handle form submissions or data modifications that require changes to the server-side data.
 ```python3
    if request.method=="POST":
 ```

###### The line `form = DataForm(request.POST)` is creating an instance of a Django form class called `DataForm` and populating it with data from the incoming `POST request`. Django forms are used to handle form data, validation, and rendering HTML forms in a consistent and reusable manner. 

###### In this example, the `DataForm` class is expected to be defined in a separate `forms.py` file within our Django app. The `form = DataForm(request.POST)` line is used to create an instance of the form with the submitted POST data. If the form is valid, we can process and save the data. If it's invalid, we can re-render the form with error messages.

###### 1) `DataForm`: This is the name of a `form` class. It's assumed that we've defined this form class somewhere in our code using Django's form` API`.

###### 2) `request.POST`: This is the data dictionary that contains the form data submitted via a `POST` request. It's part of the incoming request object.

###### 3) `form = DataForm(request.POST)`: This line creates an instance of the `DataForm` class and initializes it with the data from the `POST` request. This allows us to work with the form's data and perform validation.

 ```python3
        form=DataForm(request.POST)
 ```

###### The condition `if form.is_valid():` is used in Django to check whether the data submitted in a `form` is valid according to the form's validation rules. This is an important step before processing or saving the form data. If the form is valid, we can proceed with further actions; if not, we usually need to handle the errors and potentially show them to the user.

###### In this example, `form.is_valid()` is used to check if the form's submitted data is valid according to the form's validation rules (which we've defined in the form class). If the data is valid, we can proceed with processing and saving the cleaned data. If the data is not valid, we can re-render the form with error messages so the user knows what needs to be corrected.

###### Django's form handling and validation ensure that the data entered by users meets the defined criteria before it's used or saved in the database.

 ```python3
        if form.is_valid():
 ```
###### The line `form.save()` is used to save the data from a valid form into the database. It's typically used within a Django view function after checking that the form data is valid using the `form.is_valid()` method.

###### In this example, when `form.is_valid()` returns `True`, `form.save()` is called to save the data to the database. This line creates an instance of the model associated with the form and populates it with the cleaned data from the form. The saved instance is then returned.

###### After saving the data, we might want to perform additional actions with the instance or redirect the user to a success page.

 ```python3
            form.save()
 ```

###### The `return redirect('dashboard-predictions')` line is used to redirect the user to a specific `URL` after the form has been successfully processed and saved. In our Django application's `urls.py` file, we've assigned the name `'dashboard-predictions'` to a `URL` pattern, and we're using that name to redirect the user there.

###### In this example, when the form data is successfully saved, the redirect function is used to redirect the user to the `URL` named `'dashboard-predictions'`, which we've defined in our `urls.py` using the `path('predictions/', views.predictions, name='dashboard-predictions')` pattern.

###### Make sure that `'dashboard-predictions'` matches the name we've defined for the `URL` pattern in our `urls.py` and adjust it accordingly.

 ```python3
            return redirect('dashboard-predictions')  
 ```

###### The line `form = DataForm()` is creating an instance of a Django form class called `DataForm` without populating it with any data. This is typically used when we want to render an empty form on an initial page load, allowing the user to input data and submit the form.

###### In this example, when the request method is `"GET"` (i.e., an initial page load), a new instance of the DataForm is created without any data. This instance is then passed to the template to render the empty form for the user to fill out. If the request method is `"POST"`, the form is created using the submitted `POST` data, and the rest of the logic for form validation and processing is handled.
 

 ```python3
    else:
        form = DataForm()
 ```
###### The context dictionary we've defined is used to pass data to the template for rendering. In this case, we're passing the form instance (form) to the template so that it can be displayed and interacted with in the  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**   form.
###### In this example, the context dictionary contains a key `'form'` which maps to the form instance created in the view. When rendering the template, the values within the context dictionary are accessible, allowing us to display the form in our template.

###### In the template `**[index](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)** .html`, we can access the form fields and widgets using the 'form' key from the context dictionary, typically using Django template syntax. For example:

 ```python3
    context={
        'form':form
    }
 ```
###### The line `return render(request, "index.html", context)` is used to render an  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**  template named `"index.html"` with the provided context data. The template is used to generate the final  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**   content that will be sent to the user's browser.

###### In this example, if the request method is `"GET" (initial page load)`, a new instance of the `DataForm` is created and passed to the `'index.html'` template within the `context` dictionary. This will render the form fields in the  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**   form. If the request method is `"POST"` and the form is invalid, the same `context` dictionary is passed to the template `'index.html'` to display form errors.

###### The `render` function takes the `request` object, the template name (in this case, `'index.html'`), and the `context` dictionary. It combines the template with the context data to generate the final **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**  response.

 ```python3
    return render(request, "index.html", context) 
 ```

 ```python3
def predictions(request):
    predicted_stack=Data.objects.all()

    context={

        'predicted_stack':predicted_stack
    }

    return render(request, "predictions.html", context)
 ```
###### Let's define a `view function` named `predictions` in our Django application. View functions in Django handle incoming `HTTP` requests and return appropriate responses. Here's the start of the predictions view function:

###### In this example, the predictions view function is using the `render function` to render the  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**   template named `'predictions.html'`. We will need to replace `'predictions.html'` with the actual name of the template we want to use for rendering this view.

###### Inside the view function, we can add the necessary logic to handle the request and generate the response. This might include processing form submissions, interacting with the database, performing calculations, and preparing data to be displayed in the template.

###### As we continue to build our predictions view function, consider adding any additional logic and context data that we need to properly render the view.

 ```python3
def predictions(request):
 ```

###### The line `predicted_stack = Data.objects.all()` is querying the database to retrieve all instances of the `Data model`. It uses Django's Object-Relational Mapping (ORM) to interact with the database and retrieve the data stored in the `Data` model.

###### In this example, the `predictions` view function is retrieving all instances of the `Data` model using the `Data.objects.all()` query. The retrieved instances are stored in the `predicted_stack` variable.

###### The `context` dictionary is then created, containing the `predicted_stack` data. This context data will be passed to the `'predictions.html'` template, where we can access and display the retrieved data.

 ```python3
    predicted_stack=Data.objects.all()
 ```
###### The `context` dictionary we've defined is used to pass data to the template for rendering. In this case, we're passing the `predicted_stack` variable to the template so that we can display its contents within the  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**   template.

###### In this example, the `context` dictionary contains a key `'predicted_stack'` which maps to the `predicted_stack` variable that holds the retrieved instances of the `Data` model. When rendering the template, the values within the `context` dictionary are accessible, allowing us to display the data in our template.

###### In our template ('predictions.html'), we can access the data using the 'predicted_stack' key from the context dictionary, typically using Django template syntax. For example:

 ```python3
    context={
        'predicted_stack':predicted_stack
    }
 ```
###### The line `return render(request, "predictions.html", context)` is used to render the **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**  template named `"predictions.html"` with the provided context data. The template is used to generate the final  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**   content that will be sent to the user's browser.

###### In this example, the `context` dictionary contains the `'predicted_stack'` key, which maps to the `predicted_stack` variable holding the retrieved instances of the `Data` model. When rendering the template, the values within the context dictionary are accessible, allowing us to display the data in our template.

###### The render function takes the request object, the template name (in this case, `"predictions.html"`), and the `context` dictionary. It combines the template with the context data to generate the final  **[HTML](https://github.com/Khosiyat/GeekyPinkers/blob/main/templates.md)**  response.

 ```python3
    return render(request, "predictions.html", context)
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
