from django.apps import AppConfig


class Base1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base1'

    def ready(self):
        import base1.signals
