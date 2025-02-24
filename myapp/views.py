from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import createNewTask, createNewProject

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
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })
    #username = 'EliasDFranco'
    #'username': username
    # projects = list(Project.objects.values())
    #return JsonResponse({'projects': projects}, safe=False)
    

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    # try: 
    #   task = Task.objects.get(id=id)
    #   return HttpResponse(f'Task: {task.title}')
    #except Task.DoesNotExist:
    #    return HttpResponse('Task not found', status=404)
    
def create_task(request):
    if request.method == "GET":
        return render(request, 'tasks/create_task.html', {
            'form': createNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2
        )
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': createNewProject()
    })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
        #print(projects)
        #return render(request, 'projects/create_project.html', {
        #    'form': createNewProject()
    #})
    
def project_detail(request, id):
    project = Project.objects.get(id=id)
    get_object_or_404(Project, id=id)
    print(project)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })