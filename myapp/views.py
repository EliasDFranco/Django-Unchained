from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def HelloWorld(request, username):
    print(username)
    return HttpResponse("<h1>Hello Goodfellas, my name is Tony Soprano, i'm living in New Jersey %s </h1> " % username)

def index(request):
    return HttpResponse('Index page')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse({'projects': projects}, safe=False)

def tasks(request, id):
    try: 
        task = Task.objects.get(id=id)
        return HttpResponse(f'Task: {task.title}')
    except Task.DoesNotExist:
        return HttpResponse('Task not found', status=404)

