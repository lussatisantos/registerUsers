# Generated by Django 4.2.5 on 2023-09-28 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadUsuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='ages',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='names',
            new_name='name',
        ),
    ]
