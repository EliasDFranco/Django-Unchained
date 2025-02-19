from django.db import models

# Create your models here.
class Project(models.Model):  # Cree está clase Project
    name = models.CharField(max_length=250)
    
class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Aquí designo que project va a relacionarse con la clase Project, tmb agregue que cuando se elimine Project, 
                                                                    #se elimine en cascadsa los elementos que dependan o tengan relacion con este.
    