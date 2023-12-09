from django.urls import path, include
from .views import TaskListView, TaskCreate, TaskUpdate, TaskDelete, SignUpView

urlpatterns = [
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('task/new/', TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
     path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TaskListView.as_view(), name='home'),
    
    
]
