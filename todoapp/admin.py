from django.contrib import admin

# Register your models here.
from .models import TasksModel
admin.site.register(TasksModel)