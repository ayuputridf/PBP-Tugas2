from todolist.views import  login_user
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register 
from todolist.views import logout_user 
from todolist.views import tambah_task
from todolist.views import hapustask


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('newtask/', tambah_task, name='newtask'),
    path('hapustask/<int:pk>/', hapustask, name='hapustask'),

]