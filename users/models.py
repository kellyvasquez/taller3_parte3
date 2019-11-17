from django.db import models

# Create your models here.

from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biografia = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    foto = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return Email"""
        return self.user.username
