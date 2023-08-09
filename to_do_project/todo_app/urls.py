from django.urls import path
from .views import todo_view, add_todo_view, delete_todo_view

urlpatterns = [
    path('', todo_view, name='todo_view'),
    path('add_todo_item/', add_todo_view, name='add_todo_view'),
    path('delete_todo_item/<int:i>/', delete_todo_view, name='delete_todo_view'),
]
