# Answer of Questition 2

## Questition 2
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer

Yes, Django signals run in the same thread as the caller. This means that when a signal is sent, the connected signal handlers are executed synchronously in the same thread that triggered the signal.

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

# Runs in same thread
@receiver(post_save, sender = Person)
def person_post_save(sender, instance, created, **kwargs):
    print(f"Thread: {threading.current_thread().name}")
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

### Create Person instance
```python
$ python3 manage.py shell
Python 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from person.models import Person
>>>
>>> neha = Person(name = "Neha Chavan")
>>> neha.save()
Thread: MainThread
>>> exit()
```

### Observe the Output
When you will create a Person instance, you should see the output as `Thread: MainThread`. This means that when the caller function calls the reciver function, both the functions are executed in the same Thread.
