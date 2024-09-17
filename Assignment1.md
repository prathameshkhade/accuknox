# Answer of Questition 1

## Questition 1
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer
To determine whether Django signals are executed synchronously or asynchronously checkout the follwing code:

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

# Post save signal for Person model
@receiver(post_save, sender = Person)
def person_post_save(sender, instance, created, **kwargs):
    print(f"Person {instance.name} has been saved")
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

### Observe the Output
Go to the admin page and create an instace of Person class After saving the new instance, check the terminal You should see the output `Person ___ has been saved`.

### Conclusion

This setup confirms that the signal handling is executed synchronously because the message `Person ___ has been saved` appears immediately after saving the model instance in the Django admin.