from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def HelloWorld(request):
    return render(request, 'helloworld.html')
    # print(username)
    
def index(request): 
    title = 'Welcome to South Park!!'
    return render(request, 'index.html', {
        'titulo': title
    })

def projects(request):
    username = 'EliasDFranco'
    return render(request, 'projects.html', {
        'username': username
    })
    # projects = list(Project.objects.values())
    #return JsonResponse({'projects': projects}, safe=False)
    

def tasks(request):
    return render(request, 'tasks.html')
    # try: 
    #   task = Task.objects.get(id=id)
    #   return HttpResponse(f'Task: {task.title}')
    #except Task.DoesNotExist:
    #    return HttpResponse('Task not found', status=404)

