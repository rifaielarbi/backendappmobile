from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username =models.CharField(max_length=100, blank=True, null=True)
    email =models.EmailField(unique=True)
    first_name =models.CharField(max_length=100, blank=True, null=True)
    last_name =models.CharField(max_length=100, blank=True, null=True)   
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    dietary_preferences = models.TextField(blank=True, null=True)
    
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='custom_user_set',  # new reverse name
    blank=True
    )

    user_permissions = models.ManyToManyField(
    'auth.Permission',
     related_name='custom_user_set',  # new reverse name
     blank=True
)

    def __str__(self):
     return self.firstname + " " + self.lastname
    
    