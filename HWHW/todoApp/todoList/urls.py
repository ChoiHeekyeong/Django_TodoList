from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('writeTodo/', views.writeTodo, name='writeTodo'),
    path('delTodo/', views.delTodo, name='delTodo')
]
