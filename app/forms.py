from django.forms import ModelForm
from .models import Project


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
