from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
#=>for the signals file cause its separated , we do this to work properly
    def ready(self):
        import users.signals