# Generated by Django 4.0.3 on 2022-08-22 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_project_stack_stack_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stack',
            new_name='Language',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stack',
            new_name='major_language',
        ),
    ]
