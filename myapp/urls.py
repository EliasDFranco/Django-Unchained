from django.urls import path
from . import views 

# Creamos un nuevo archivo "urls.py" pero en la app "myapp", cada app tendrá que almacenar sus propias urls
urlpatterns = [
    path('', views.index, name="index"), #Creando URL names
    path('HelloWorld/', views.HelloWorld, name="HelloWorld"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_tasks"),
    path('create_project/', views.create_project, name="create_project"),
    
]   
#La función include de Django en Python permite incluir contenido de una plantilla dentro de otra.
# Esto es útil cuando se tiene el mismo contenido para varias páginas.

#La función include() de django.conf.urls toma una ruta de importación completa de Python a otro módulo URLconf. 
