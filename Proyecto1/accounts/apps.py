from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    # Comentá o quitá el método ready() que llama a signals:
    # def ready(self):
    #     import accounts.signals