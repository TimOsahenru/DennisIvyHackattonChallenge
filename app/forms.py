from django.forms import ModelForm
from .models import Project, User


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


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_nos', 'country', 'years_of_experience',
                  'avatar', 'langauge', 'about', 'github']



