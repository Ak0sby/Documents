from django.apps import AppConfig

class DiagramAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diagram_app'

    def ready(self):
        import diagram_app.signals # Бул жерде signals.py иштетилет
