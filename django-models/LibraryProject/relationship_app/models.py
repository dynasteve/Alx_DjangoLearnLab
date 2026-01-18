from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=150)
  
  def __str__(self):
      return self.name
  
class Book(models.Model):
  title = models.CharField(max_length=150)
  publication_year = models.PositiveIntegerField(default=timezone.now().year, null=True, blank=True)
  author = models.ForeignKey(Author, verbose_name="author", on_delete=models.CASCADE, related_name="books")
  
  def __str__(self):
      return self.title
  
class Library(models.Model):
  name = models.CharField(max_length=150)
  books = models.ManyToManyField(Book, related_name='libraries')
  
  def __str__(self):
      return self.name
  
  
class Librarian(models.Model):
  name = models.CharField(max_length=150)
  library = models.OneToOneField(Library, related_name='librarian', on_delete=models.CASCADE)
  
  def __str__(self):
      return self.name
    
    
class UserProfile(User):
  role_choices = [
    ('admin', "Admin"),
    ('librarian', 'Librarian'),
    ('member', 'Member'),
  ]
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
  role = models.CharField(max_length=50, choices=role_choices)
  
  def __str__(self):
     return f"{self.user.username} has role {self.role}"
   
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='member')
