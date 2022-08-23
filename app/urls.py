from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects'),
    path('create-project', views.project_create, name='create-project'),
    path('update-project/<int:pk>/', views.project_update, name='update-project'),
    path('delete-project/<int:pk>/', views.project_delete, name='delete-project'),
]
