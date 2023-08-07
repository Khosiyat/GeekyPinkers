#### This repository is for educational purposes. 
**[watch the tutorial](https://www.youtube.com/playlist?list=PLoRaeB82EdK6ZIdpklyBUj7qWhvbVDCw- )**


1. **[Introduction]( https://youtu.be/gWZf-mR1IgM)**
2. **[Machine Learning Model Training](https://youtu.be/QI6zEqf8QYw)**
3. **[Install Django](https://youtu.be/32EdUDkiQKY)**
4. **[Model](https://youtu.be/w-4QLspvmXM)**
5. **[Forms & Views](https://youtu.be/3ECIXMr8qTo )**
6. **[Templates](https://youtu.be/er5UtdYBdqQ )**



# GeekyPinkers

**[Download Python](https://www.python.org/downloads/ )**

**[Install Django](https://docs.djangoproject.com/en/4.2/topics/install/ )**

**[Install Other Packages](https://pypi.org/project/joblib/ )**


-Copy past followings onto your command prompt:

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
pip install Django
pip install scikit-learn
pip install joblib
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
You may try it yourself using the [google colab](https://colab.google/notebooks/ ) or [jupyter notebook](https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled5.ipynb).

-This is a small dataset we used in this project. In real-world projects, you are supposed to work with big data:
> https://github.com/Khosiyat/GeekyPinkers/blob/main/geekyPinkers_dataset.csv





**In-person events:**

| WHEN?  |WHAT TO LEARN?  |
| ------------- | ------------- |
| Week 1  | Train Machine Learning Model  |
| Week 2  | Install Django, Create Django Model  |
| Week 3  | Django views, URLs   |
| Week 4  | Django Forms and Templates  |
| Week 5  | A. Divide into three teams: 1) machine learning/model training 2) back-end 3) front-end B. Plan to build X web application (like GeekyPinkers)  |
| Week 6  | Present the Demo of the X web application  |
