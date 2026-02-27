from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

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
  
  # models.TextField()
  
  class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # prevents duplicate likes

    def __str__(self):
        return f"{self.user} liked {self.post}"