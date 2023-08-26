
#### index.html
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
