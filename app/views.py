from django.shortcuts import render


def project_list(request):

    context = {}
    return render(request, 'index.html', context)
