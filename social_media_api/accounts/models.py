from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
  bio = models.TextField(max_length=1000, blank=True)
  profile_picture = models.ImageField(blank=True, null=True)
  followers = models.ManyToManyField('self', symmetrical=False, related_name='Following', blank=True)
  following = models.ManyToManyField('self', symmetrical=False, related_name='Followers', blank=True)
  
  def __str__(self):
      return self.username
  