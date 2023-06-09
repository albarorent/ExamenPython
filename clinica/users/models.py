from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class usuario(AbstractUser):
    username = models.CharField(max_length=25, primary_key=True)
    full_name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False)
    telefono = models.CharField(max_length=25,null=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELD = ["full_name", "email","telefono"]

    class Meta:
        db_table = "usuarios"
