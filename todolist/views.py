from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from todolist.forms import TaskForm
from datetime import date

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user=request.user).all()
    context = {
        'isi_todo_list': data,
        'name': 'Ayu Putri DF',
        'id': '2106654845',
    }
    return render(request, "todolist.html", context)

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                date = str(date.today()),
                title = form.cleaned_data["task_title"],
                description = form.cleaned_data["task_description"],
                user = request.user,
            )
            task.save()
            messages.success(request, 'Task berhasil dibentuk')
            return redirect('todolist:show_todolist')
    context = {"form": form}
    return render(request, 'create_task.html', context)

def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return redirect('todolist:show_todolist')

def change_status(request, id):
    task = Task.objects.get(pk=id) 
    if (not task.is_finished):
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'Berhasil logout')
    return redirect('todolist:login')