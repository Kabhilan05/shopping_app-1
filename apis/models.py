from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
