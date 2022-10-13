from asyncio import create_task
from django.urls import path
from unicodedata import name

# from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import ubah_status
from todolist.views import hapus_task
from todolist.views import show_json
from todolist.views import show_todolist_ajax
from todolist.views import add_task


app_name = 'todolist'

urlpatterns = [
    # path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('ubah-status/<int:id>', ubah_status, name='ubah_status'),
    path('hapus-task/<int:id>', hapus_task, name='hapus_task'),
    path('json/', show_json, name='show_json'),
    path('', show_todolist_ajax, name='show_todolist_ajax'),
    path('add/', add_task, name='add_task'),

]