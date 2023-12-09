from django.shortcuts import render

from category.models import CategoryModel
from task.models import TaskModel


def base(request):
    return render(request, 'base.html')

def show_tasks(request):
    categories = CategoryModel.objects.all()
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'categories': categories, 'tasks': tasks})