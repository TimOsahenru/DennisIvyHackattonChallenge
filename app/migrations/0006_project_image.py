# Generated by Django 4.0.3 on 2022-08-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='1.png', null=True, upload_to=''),
        ),
    ]