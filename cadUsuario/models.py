from django.db import models

class Users(models.Model):
    id_users = models.AutoField(primary_key=True)
    names = models.TextField(max_length=255)
    ages = models.IntegerField()
