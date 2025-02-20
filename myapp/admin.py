from django.contrib import admin
from .models import Project, Task 

# Register your models here.
admin.site.register(Project)  #Para abrir una sección nueva en Django admin
admin.site.register(Task)