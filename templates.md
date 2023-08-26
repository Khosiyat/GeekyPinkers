
#### index.html

Let's reference {{form.worked_fields}}, which appears to be a template tag or variable within a Django template. In Django's template system, you use double curly braces {{ ... }} to output dynamic content onto your HTML page. Let's break down what this might mean in the context of a Django template:

{{ ... }}: This is the syntax for outputting dynamic content in a Django template.

form.worked_fields: This suggests that you are attempting to access a variable or attribute called worked_fields within a form object.

Assuming you have a Django form object with a field named worked_fields, the code you provided would render the value of the worked_fields field in your template. For example, if you had a form like this:

Let's render this form in a template, using {{ form.worked_fields }} in the template would display the input field for the worked_fields field of the form.

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

uses template tags to iterate over a list (predicted_stack) and generate HTML <tr> elements for each item in the list. Each item in the list seems to have attributes like name and predictions, which are being displayed in the table cells using the {{ ... }} template syntax.

Here's a breakdown of the code:

{% for i in predicted_stack %}: This initiates a loop that iterates over each item (i) in the predicted_stack list.

<tr>: This HTML tag represents a table row, which will contain table cells.

<th>{{i.name}}</th>: This defines a table header cell (<th>) that displays the name attribute of the current item i.

<th>{{i.predictions}}</th>: This defines another table header cell that displays the predictions attribute of the current item i.

{% endfor %}: This marks the end of the loop.

You can adjust the HTML structure and CSS styling as needed to fit your design.

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
