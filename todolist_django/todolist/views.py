from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login, logout
from .forms import RegUserForm, LogUserForm
from .models import ToDo

# Create your views here.

def RegUser(request):
    if request.method == 'POST':
        form = RegUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('todo')
    else:
        form = RegUserForm()
    return redirect('todo')

def LogUser(request):
    if request.method == 'POST':
        form = LogUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect('todo')
    else:
        form = LogUserForm()
    return redirect('todo')

def LogoutUser(request):
    logout(request)
    return redirect('todo')

def add_el(request, user_id):
    add_info = request.GET.get('add_info')
    item_add = ToDo.objects.create(user_id=user_id, todo=str(add_info))
    item_add.save()
    return redirect('todo')


def del_el(request, user_id, item_id):
    # do_id = request.GET.get('item_id')
    # user_id = request.GET.get('user_id')
    item = ToDo.objects.get(pk=item_id, user = user_id)
    item.delete()
    return redirect('todo')

def del_el_all(request, user_id):
    for item in ToDo.objects.filter(user_id=user_id):
        item.delete()
    return redirect('todo')

class ToDoView(ListView):
    model = ToDo
    template_name = 'todolist/todo.html'
    context_object_name = 'do'
    extra_context = {'reg': RegUserForm, 'log': LogUserForm}

    def get_queryset(self):
        return ToDo.objects.filter(user = self.request.user.id)