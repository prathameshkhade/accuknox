# Solution of Questions for AccuKnox

The project structure is as follows with `src` is parent folder and `project` is the name of the project and `person` is the app.

```sh
.
├── Assignment1.md
├── Assignment2.md
├── Assignment3.md
├── README.md
├── Rectangle.py
├── src
    ├── db.sqlite3
    ├── manage.py
    ├── person
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── signals.py
    │   ├── tests.py
    │   └── views.py
    └── project
        ├── __init__.py
        ├── __pycache__
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## Question 1: [Answer](./Assignment1.md)
## Question 2: [Answer](./Assignment2.md)
## Question 3: [Answer](./Assignment3.md)
## Question 4: 
### Topic: Custom Classes in Python
#### Description: You are tasked with creating a Rectangle class with the following requirements:
1.  An instance of the Rectangle class requires length:int and width:int to be initialized.
2.  We can iterate over an instance of the Rectangle class
3.  When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

### Answer
> [!TIP]
> Refer [Rectangle.py](./Rectangle.py)

```python
class Rectangle():
    """
    Represents the the Rectangle
    """

    def __init__(self, length:int, width:int) -> None:
        self.length = length
        self.width = width

    def __iter__(self):
        # Reset the iter_index for each instance
        self._iter_index = 0
        return self
    
    def __next__(self):
        if self._iter_index == 0:
            self._iter_index += 1
            return {'length': self.length}
        elif self._iter_index == 1:
            self._iter_index += 1
            return {'width': self.width}
        else:
            raise StopIteration

# Create an instance of Rectangle class
rectangle = Rectangle(10, 20)

# Iterate through the instance
for item in rectangle:
    print(item)
```

Run the Python file to see the output

```bash
$ python3 Rectangle.py

{'length': 10}
{'width': 20}
```