from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectUpdateForm, ProjectCreateForm


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
def project_update(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectUpdateForm(instance=project)
    # programmer = request.user

    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            # return redirect('profile', pk=programmer.id)
            return redirect('projects')
    context = {'form': form}
    return render(request, 'create-edit-project.html', context)


# ................... Project Delete ...................
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
def project_create(request):
    page = 'create'
    form = ProjectCreateForm
    # programmer = request.user

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid:
            project = form.save(commit=False)
            project.programmer = request.user
            project.save()
            # return redirect('profile', pk=programmer.id)
            return redirect('projects')

    context = {'form': form, 'page': page}
    return render(request, 'create-edit-project.html', context)

def register(request):
    return render(request, 'signup.html', {})

def login(request):
    return render(request, 'login.html', {})

