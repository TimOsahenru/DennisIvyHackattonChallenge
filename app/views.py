from django.shortcuts import render


def project_list(request):

    context = {}
    return render(request, 'home.html', context)

def register(request):
    return render(request, 'signup.html', {})

def login(request):
    return render(request, 'login.html', {})

