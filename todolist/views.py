from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from todolist.models import ToDoList
from todolist.forms import ToDoListForm 
from datetime import date

from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse 


# Create your views here.
# def show_todolist(request):
#     data = ToDoList.objects.filter(user=request.user).all()
#     context = {
#         'isi_todo_list': data,
#         'name': 'Ayu Putri',
#         'id': '2106654845',
#     }
#     return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    data = ToDoList.objects.filter(user=request.user).all()
    context = {
        'todo_list': data,
    } 
    return render(request, "todolist_ajax.html", context)

def show_json(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = ToDoList(
            date=str(date.today()),
            title=title, 
            description=description,
            user=request.user,
        )
        new_task.save()
    return redirect('todolist:show_todolist_ajax')

def create_task(request):
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
            return redirect('todolist:show_todolist_ajax')
    context = {"form": form}
    return render(request, 'create_task.html', context)

def ubah_status(request, id):
    data = ToDoList.objects.get(pk=id) 
    if (not data.is_finished):
        data.is_finished = True
    data.save()
    return redirect('todolist:show_todolist_ajax')

def hapus_task(request, id):
    ToDoList.objects.get(pk=id).delete()
    return redirect('todolist:show_todolist_ajax')


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
            return redirect('todolist:show_todolist_ajax')
        else:
            messages.info(request, 'Wrong Username or Password, try again!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'Successfully logout, see ya!^^')
    return redirect('todolist:login')


