from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.create_task, name = 'create_task'),
    path('read', views.read_task, name = 'read_task'),
    path('update/<int:id>', views.update_task, name = 'update_task'),
    path('delete/<int:id>', views.delete_task, name = 'delete_task'),

]