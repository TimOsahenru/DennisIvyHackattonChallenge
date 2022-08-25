from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]