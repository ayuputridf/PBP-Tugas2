from django.shortcuts import render
from todolist.models import ToDoList
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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
    context = {}
    if request.method == "POST":
        data = ToDoList(user=request.user, title=request.POST.get('whattodo'), description=request.POST.get('description'))
        data.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html",context)

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
    return redirect('todolist:login')