from django.contrib import admin

# Register your models here.
from .models import Task , Integrations 

admin.site.register(Task)
admin.site.register(Integrations)