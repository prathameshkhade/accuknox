from .models import Person
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

# Synchonous signal
# @receiver(post_save, sender = Person)
# def person_post_save(sender, instance, created, **kwargs):
#     print(f"Person {instance.name} has been saved")

# Runs in same thread
@receiver(post_save, sender = Person)
def person_post_save(sender, instance, created, **kwargs):
    print(f"Thread: {threading.current_thread().name}")