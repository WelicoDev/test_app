from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="profile_default_picture.jpg", upload_to='profile_image')


    def save(self, *args, **kwargs):
        super().save()

    def __str__(self):
        return self.username

