from django.urls import path
from . import views 

# Creamos un nuevo archivo "urls.py" pero en la app "myapp", cada app tendrá que almacenar sus propias urls
urlpatterns = [
    path('', views.index),
    path('HelloWorld/', views.HelloWorld),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    
]   
#La función include de Django en Python permite incluir contenido de una plantilla dentro de otra.
# Esto es útil cuando se tiene el mismo contenido para varias páginas.

#La función include() de django.conf.urls toma una ruta de importación completa de Python a otro módulo URLconf. 
