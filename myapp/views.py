from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import Task
from .forms import TaskForm

@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'myapp/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(usuario=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'myapp/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_form_kwargs(self):
        kwargs = super(TaskCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'myapp/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(usuario=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDelete(DeleteView):
    model = Task
    template_name = 'myapp/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(usuario=self.request.user)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def task_list(request):
    tasks = Task.objects.filter(usuario=request.user)
    return render(request, 'myapp/task_list.html', {'tasks': tasks})
