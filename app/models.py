from django.db import models
from django.contrib.auth.models import AbstractUser


class Language(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    phone_nos = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    langauge = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    github = models.URLField(max_length=500, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Project(models.Model):
    programmer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    git_url = models.CharField(max_length=2000, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    major_language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(null=True, default=None)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.programmer.username

    class Meta:
        ordering = ['created_at']
