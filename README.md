# DS

[http://green-foot-app.herokuapp.com](http://green-foot-app.herokuapp.com)

Takes in json file with key = `car_distance` and `bus_distance` with values of `int` or `float` in `km`.

Returns the CO2 equivalent emission in lbs per car on gasoline/diesel and per passenger on bus.

Sample input:

`input = {"car_distance": 277.093,
          "bus_distance": 281.248}`


Sample Response:


```python
{'Pounds of CO2E emission per car on gasoline (22 mpg)': 155.10192509045453,
'Pounds of CO2E emission per car on diesel (22 mpg)': 177.67500405218186,
'Pounds of CO2E emission per passenger on bus': 37.00631578947368}
```
