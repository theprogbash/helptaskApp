from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from helpdesk_app.forms import CreateTaskForm
from helpdesk_app.models import Task

def index(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uşaqlar indi müraciətinizə baxacaq.')
            return HttpResponseRedirect('/')
    else:
        form = CreateTaskForm(use_required_attribute=False)
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def table(request):
    tasks = Task.objects.all().order_by('-task_created_date')
    context = {
        'tasks': tasks,
    }
    return render(request, 'table.html', context)