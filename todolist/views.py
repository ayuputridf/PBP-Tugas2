from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

from todolist.models import ToDoList
from todolist.forms import ToDoListForm
from datetime import date

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = ToDoList.objects.filter(user=request.user)
    context = {
        'isi_todolist': data_todolist,
        'nama': request.user.username,
        }
    return render(request, "todolist.html", context)


def tambah_task(request):
    form = ToDoListForm()
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            data = ToDoList(
                date = str(date.today()),
                title = form.cleaned_data["task_title"],
                description = form.cleaned_data["task_description"],
                user = request.user,
            )
            data.save()
            messages.success(request, 'Your task successfully created!')
            return redirect('todolist:show_todolist')
    context = {"form": form}
    return render(request, 'create_task.html', context)

    # context = {}
    # if request.method == "POST":
    #     data = ToDoList(user=request.user, title=request.POST.get('whattodo'), description=request.POST.get('description'))
    #     data.save()
    #     return redirect('todolist:show_todolist')
    
    # return render(request, "create-task.html",context)

def hapustask(request, pk):
    data = ToDoList.objects.filter(pk=pk)
    data.delete()
    return redirect('todolist:show_todolist')
 
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
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
            messages.info(request, 'Wrong username or password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'Successfully logout, see you^^')
    return redirect('todolist:login')