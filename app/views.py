from django.shortcuts import render, redirect
from .models import Project, User
from .forms import ProjectUpdateForm, ProjectCreateForm, UserProfileForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.messages.views import messages
from django.contrib.auth.decorators import login_required


# ................... Profile ...................
def profile(request, pk):

    programmer = User.objects.get(id=pk)
    my_projects = programmer.project_set.all()

    context = {'programmer': programmer, 'my_projects': my_projects}
    return render(request, 'profile.html', context)


# ................... Profile Update...................
@login_required(login_url='login')
def profile_update(request):
    form = UserProfileForm(instance=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=request.user.id)

    context = {'form': form}
    return render(request, 'profile-update.html', context)


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
    user = request.user

    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)
    context = {'form': form}
    return render(request, 'create-edit-project.html', context)


# ................... Project Delete ...................
@login_required(login_url='login')
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user
    if request.method == 'POST':
        project.delete()
        return redirect('profile', pk=user.id)

    context = {'project': project}
    return render(request, 'delete-confirm.html', context)


# ................... Project Create .................
@login_required(login_url='login')
def project_create(request):
    page = 'create'
    form = ProjectCreateForm()
    user = request.user

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.programmer = user
            project.save()
            return redirect('profile', pk=user.id)

    context = {'form': form, 'page': page}
    return render(request, 'create-edit-project.html', context)


# ................... Login User ...................
def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile', pk=user.id)
            # return redirect('projects')

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
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # return redirect('profile', pk=user.id)
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')

    context = {}
    return render(request, 'login-register.html', context)
