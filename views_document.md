**[Watch video about this Views and Forms](https://youtu.be/zcGjaVg9iHk?si=otKmMDNqU6xGeCop)**
 ```python3
from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
 ```

 ```python3
from django.shortcuts import render, redirect
 ```

 ```python3
from .forms import DataForm
 ```

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

 ```python3
def index(request):
 ```

 ```python3
    if request.method=="POST":
 ```

 ```python3
        form=DataForm(request.POST)
 ```

 ```python3
        if form.is_valid():
 ```

 ```python3
            form.save()
 ```

 ```python3
            return redirect('dashboard-predictions')  
 ```

 ```python3
    else:
        form = DataForm()
 ```

 ```python3
    context={
        'form':form
    }
 ```

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

 ```python3
def predictions(request):
 ```

 ```python3
    predicted_stack=Data.objects.all()
 ```

 ```python3
    context={
        'predicted_stack':predicted_stack
    }
 ```

 ```python3
    return render(request, "predictions.html", context)
 ```
