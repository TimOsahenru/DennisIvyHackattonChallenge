from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects'),
    path('project-detail/<int:pk>/', views.project_detail, name='project-detail'),
    path('update-project/<int:pk>/', views.project_update, name='update-project'),
    path('delete-project/<int:pk>/', views.project_delete, name='delete-project'),
    path('create-project/', views.project_create, name='create-project'),


    path('register/', views.signup_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('profile/<int:pk>/', views.profile, name='profile'),
]