from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectCreateForm, ProjectUpdateForm


def project_update(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectUpdateForm(instance=project)

    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'create-edit-project.html', context)


def project_create(request):
    page = 'create'
    form = ProjectCreateForm

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('projects')

    context = {'form': form, 'page': page}
    return render(request, 'create-edit-project.html', context)


def project_list(request):
    projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'index.html', context)


def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'project': project}
    return render(request, 'delete-confirm.html', context)
