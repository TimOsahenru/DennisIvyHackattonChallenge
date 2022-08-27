from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectUpdateForm, ProjectCreateForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.messages.views import messages
from django.contrib.auth.decorators import login_required


# ................... All Projects ...................
def project_list(request):
    projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'home.html', context)


# ................... Project Detail ...................
def project_detail(request, pk):
    project = Project.objects.get(id=pk)

    context = {'project': project}
    return render(request, 'project-detail.html', context)


# ................... Project Update ...................
@login_required(login_url='login')
def project_update(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectUpdateForm(instance=project)
    # programmer = request.user

    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            # return redirect('profile', pk=programmer.id)
            return redirect('projects')
    context = {'form': form}
    return render(request, 'create-edit-project.html', context)


# ................... Project Delete ...................
@login_required(login_url='login')
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    # programmer = request.user
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
        # return redirect('profile', pk=programmer.id)

    context = {'project': project}
    return render(request, 'delete-confirm.html', context)


# ................... Project Create .................
@login_required(login_url='login')
def project_create(request):
    page = 'create'
    form = ProjectCreateForm()
    # programmer = request.user

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.programmer = request.user
            project.save()
            # return redirect('profile', pk=programmer.id)
            return redirect('projects')

    context = {'form': form, 'page': page}
    return render(request, 'create-edit-project.html', context)


# ................... Login User ...................
def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return redirect('profile', pk=user.id)
            return redirect('projects')

    context = {'page': page}
    return render(request, 'login-register.html', context)


# ................... Logout User ...................
def logout_user(request):
    logout(request)
    return redirect('projects')


# ................... SignUp User ...................
def signup_user(request):

    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                # return redirect('profile', pk=user.id)
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')

    context = {}
    return render(request, 'login-register.html', context)
