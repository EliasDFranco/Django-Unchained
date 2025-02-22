from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import createNewTask

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
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
    # try: 
    #   task = Task.objects.get(id=id)
    #   return HttpResponse(f'Task: {task.title}')
    #except Task.DoesNotExist:
    #    return HttpResponse('Task not found', status=404)
    
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {
            'form': createNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2
        )
        return redirect('tasks/')
