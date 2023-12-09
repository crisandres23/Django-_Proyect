"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import TaskListView, TaskCreate, TaskUpdate, TaskDelete, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(), name='home'),
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('task/new/', TaskCreate.as_view(), name='task_create'),
    path('signup_view/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('myapp/', include('myapp.urls')),
    path('', TaskListView.as_view(), name='home'),
    
]

