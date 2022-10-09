from django.urls import path

from . import views

app_name="todoapp"
urlpatterns = [
    
	path('to-do-list', views.toDoList, name="to-do-list"),
    path('mark-this-task-complete/<str:pk>/', views.markTaskComplete, name="markTaskComplete"),
    
    path('completed-tasks', views.completedTasksList, name="completedTasksList"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('update_tasks/<str:pk>/', views.update_tasks, name="update_tasks"),

	
] 