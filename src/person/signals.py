from .models import Person
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
from django.db import transaction

# Synchonous signal
# @receiver(post_save, sender = Person)
# def person_post_save(sender, instance, created, **kwargs):
#     print(f"Person {instance.name} has been saved")

# Runs in same thread
# @receiver(post_save, sender = Person)
# def person_post_save(sender, instance, created, **kwargs):
#     print(f"Thread: {threading.current_thread().name}")

# Runs on the same database transaction
@receiver(post_save, sender = Person)
def person_post_save(sender, instance, **kwargs):
    with transaction.atomic():
        if not Person.objects.filter(name = "Signal Person").exists():
            Person.objects.create(name = "Signal Person")
            print("Signal Person has been created")
        raise Exception("Signal Person is already created")