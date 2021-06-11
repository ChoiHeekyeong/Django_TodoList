from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'todoList/index.html', content)

def writeTodo(request):
    title = request.POST['todoContent']
    new_todo = Todo(content = title)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


def delTodo(request):
    end_todo_id = request.GET['todoIndex']
    todo = Todo.objects.get(id = end_todo_id)
    todo.isDone = True
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

