from django.db import models

class Users(models.Model):
    id_users = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    age = models.IntegerField()
