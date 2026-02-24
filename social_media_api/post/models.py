from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
  author = models.ForeignKey(User, related_name='post_author' ,on_delete=models.CASCADE)
  title = models.CharField(max_length=250)
  content = models.TextField(max_length=2000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
  
class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
  author = models.ForeignKey(User, related_name='author' ,on_delete=models.CASCADE)
  content = models.TextField(max_length=2000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"comment by {self.author.username} to {self.post}"