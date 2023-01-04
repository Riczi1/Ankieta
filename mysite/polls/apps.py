from django.contrib import admin

from .models import Question

admin.site.register(Question)

class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
