**[Watch Vieo about this Templates](https://youtu.be/MxpcVszpVgc?si=wYy1lsKjOILYT3l0)**

#### index.html

Let's reference `{{form.worked_fields}}`, which appears to be a template tag or variable within this `index` Django template:

1) `{{ ... }}`: This is the syntax for outputting dynamic content in a Django template.

2) `form.worked_fields`: This suggests that we are attempting to access a variable or attribute called `worked_fields` within a form object.

We have a Django **[form](https://github.com/Khosiyat/GeekyPinkers/blob/main/form_document.md)** object with a fields named `worked_fields`, `academic_fields`, `worked_industry`, ``invested_time. And the code we provided would render the value of the these fields in our template.

This template would display the input field for the `worked_fields`, `academic_fields`, `worked_industry`, ``invested_time  fields of the form.

```
                 <table>
                <tr> 
                    <th scope="row"> {{form.name}}</th>
                    <td>  {{form.worked_fields}} </td>
                    <td> {{form.academic_fields}}</td>
                    <td>  {{form.worked_industry}}</td>
                    <td> {{form.invested_time}} </td>
                </tr>
                </table>
```


#### predictions.html

In the below, we use template tags to iterate over a list `predicted_stack` (see **[model](https://github.com/Khosiyat/GeekyPinkers/blob/main/model_document.md)** and **[view](https://github.com/Khosiyat/GeekyPinkers/blob/main/views_document.md)** ) and generate HTML `<tr>` elements for each item in the list. Each item in the list seems to have attributes like name and predictions, which are being displayed in the table cells using the `{{ ... }}` template syntax:

1) `{% for i in predicted_stack %}`: This initiates a loop that iterates over each item `i` in the `predicted_stack` list.

2) `<tr>`: This HTML tag represents a table row, which will contain table cells.

3) `<th>{{i.name}}</th>`: This defines a table header cell `<th>` that displays the name attribute of the current item `i`.

4) `<th>{{i.predictions}}</th>`: This defines another table header cell that displays the predictions attribute of the current item `i`.

5) `{% endfor %}`: This marks the end of the loop.

- We can adjust the HTML structure and CSS styling as needed to fit our design.

```
                <table>
                    <tbody>
                        {% for i in predicted_stack %}
                        <tr>
                            <th>{{i.name}}</th>
                            <th>{{i.predictions}}</th>
                        </tr>
                        {% endfor %}
                    </tbody> 
                </table>

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
