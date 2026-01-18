from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=150)
  
  def __str__(self):
      return self.name
  
class Book(models.Model):
  title = models.CharField(max_length=150)
  author = models.ForeignKey("Author", verbose_name="author", on_delete=models.CASCADE, related_name="author")
  
  def __str__(self):
      return self.title
  
class Library(models.Model):
  name = models.CharField(max_length=150)
  books = models.ManyToManyField("Book", related_name='books')
  
  def __str__(self):
      return self.name
  
  
class Librarian(models.Model):
  name = models.CharField(max_length=150)
  library = models.OneToOneField("Library", related_name='library', on_delete=models.CASCADE)
  
  def __str__(self):
      return self.name
    