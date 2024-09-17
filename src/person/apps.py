from django.apps import AppConfig


class PersonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'person'

    def ready(self) -> None:
        import person.signals
