from django.contrib import admin
from .models import Project, Language, User


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Language)

