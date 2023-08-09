from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import TodoListItem


def todo_view(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todo_app/todo_list.html', {'all_items': all_todo_items})


def add_todo_view(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            new_item = TodoListItem(content=content)
            new_item.save()
    return HttpResponseRedirect(reverse('todo_view'))


def delete_todo_view(request, i):
    item = get_object_or_404(TodoListItem, id=i)
    item.delete()
    return HttpResponseRedirect(reverse('todo_view'))
