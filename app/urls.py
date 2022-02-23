from django.urls import path
from app import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Create task.
    path('create/', views.create, name='create'),
    # Show all created tasks.
    path('create_list/', views.create_list, name='create_list'),
    # Show active task details.
    path('task_details/<str:pk>/', views.task_details, name='task_details'),
    # Show active task.
    path('active_task/', views.active_task, name='active_task'),
    # Show assigned task.
    path('assigned_task/', views.assigned_task, name='assigned_task'),
    # Show complete task.
    path('complete_task/', views.complete_task, name='complete_task'),
    # Show upcoming task.
    path('upcoming_task/', views.upcoming_task, name='upcoming_task'),
    # Show overdue task.
    path('overdue_task/', views.overdue_task, name='overdue_task'),
    # Edit task.
    path('edit_task/<str:pk>/', views.edit_task, name='edit_task'),
    # Delete task.
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
]