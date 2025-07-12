from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Age= models.IntegerField(default=0)


