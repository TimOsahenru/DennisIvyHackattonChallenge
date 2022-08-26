from django.forms import ModelForm
from .models import Project
from django.contrib.auth.models import User


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['programmer']


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['programmer']
