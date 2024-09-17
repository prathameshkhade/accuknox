# Answer of Questition 3

## Questition 3
Question 3: By default do django signals run in the same database transaction as the caller?
Please support your answer with a code snippet that conclusively proves your stance. The code
does not need to be elegant and production ready, we just need to understand your logic.

## Answer
Yes, by default, Django signals run in the same database transaction as the caller. This means that any changes made by the signal handlers are part of the same transaction and will be committed or rolled back together with the caller's transaction.

Consider the following example of the code

### person/models.py
```python
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
```
### person/signals.py
```python
from .models import Person
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

# Runs on the same database transaction
@receiver(post_save, sender = Person)
def person_post_save(sender, instance, **kwargs):
    with transaction.atomic():
        if not Person.objects.filter(name = "Signal Person").exists():
            Person.objects.create(name = "Signal Person")
            print("Signal Person has been created")
```

### person/apps.py
```python
from django.apps import AppConfig


class PersonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'person'

    def ready(self) -> None:
        import person.signals
```
### person/admin.py
```python
from django.contrib import admin

# Import the model
from .models import Person

# Register your models here.
admin.site.register(Person)
```

### Create Person instance | Test 1
```python
# python3 manage.py shell

Python 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from person.models import Person
>>>
>>> # List of all Person
>>> print(Person.objects.all())
<QuerySet [<Person: Rhea Chakraboty>, <Person: Disha Patani>, <Person: Neha Chavan>]>
>>>
>>> # Create a new instance
>>> dua = Person(name = "Dua Lipa")
>>> dua.save()
Signal Person has been created
>>>
>>> print(Person.objects.all())
<QuerySet [<Person: Rhea Chakraboty>, <Person: Disha Patani>, <Person: Neha Chavan>, <Person: Dua Lipa>, <Person: Signal Person>]>
>>>
now exiting InteractiveConsole...
```
After saving the new instace of Person (with name = "Dua Lipa"), the `Signal Person` also created.


### Create Person instance | Test 2

### person/signals.py | Modify
Let's change `signals.py` file to intentionally raise an Exception.

```python
# person/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person
from django.db import transaction

@receiver(post_save, sender=Person)
def person_post_save(sender, instance, **kwargs):
    with transaction.atomic():
        if not Person.objects.filter(name='Signal Person').exists():
            Person.objects.create(name='Signal Person')
        raise Exception("Signal Person is already created")
```

Save the file and now try to create an instace of Person class with python shell or Admin panel.

```python
Python 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from person.models import Person
>>>
>>> # Create and save a Person instance
>>> person = Person(name = "Prathamesh")
>>> person.save()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/prathamesh/projects/accuknox/venv/lib/python3.11/site-packages/django/db/models/base.py", line 891, in save
    self.save_base(
  File "/home/prathamesh/projects/accuknox/venv/lib/python3.11/site-packages/django/db/models/base.py", line 1012, in save_base
    post_save.send(
  File "/home/prathamesh/projects/accuknox/venv/lib/python3.11/site-packages/django/dispatch/dispatcher.py", line 189, in send
    response = receiver(signal=self, sender=sender, **named)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/prathamesh/projects/accuknox/src/person/signals.py", line 24, in person_post_save
    raise Exception("Signal Person is already created")
Exception: Signal Person is already created
>>>
now exiting InteractiveConsole...
```

### Conclusion
In the Test 1, the `Signal Person` entry is created because the signal handler runs within the same transaction as the `Person` instance save. In the Test 2, due to an intentional exception, the transaction is rolled back, and the `Signal Person` entry is not created, demonstrating that signal handlers are part of the same database transaction as the original operation.