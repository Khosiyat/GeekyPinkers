#### This repository is for educational purposes. 
# GeekyPinkers

Copy past followings onto your command prompt:

1. Clone the GeekyPinkers Project.
```
git clone https://github.com/Khosiyat/GeekyPinkers.git
```

2. The GeekyPinkers Project is cloned to your local machine. Now, you may copy and paste the followings into the command prompt. About the command prompt: (you may open it from the directory as shown in the video).

-Activate local environment: go to the script directory and activate
```python3
activate
```

-It is required to install necessary packages and libraries. Install them by writing the followings in the command prompt:
```python3
pip install Python
pip install Django
pip install PIL
pip install pandas
.......
```

- Go back to the "...\geekyPinkersProject" folder (please follow the instructions shown in the video) and make migrations
```python3
python manage.py makemigrations
```

- Migrate
```python3
python manage.py migrate
```

- Runserver
```python3
python manage.py runserver
```


- Create a super user (please follow the instructions shown in the video) 
```python3
python manage.py createsuperuser
```



**Note:**
-The ML model we trained in the colab.google is provided in this repository:
> https://github.com/Khosiyat/GeekyPinkers/blob/main/geekyPinkers_project.ipynb
You may try it yourself using the colab.google/notebooks/ or jupyter.org notebook.

-This is a small dataset we used in this project. In real-world projects, you are supposed to work with big data:
> https://github.com/Khosiyat/GeekyPinkers/blob/main/geekyPinkers_dataset.csv
