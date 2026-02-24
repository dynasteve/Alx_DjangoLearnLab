from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
  author = serializers.ReadOnlyField(source='author.username')

  class Meta:
    queryset = Comment
    fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
    read_only_fields = ['author']
  

class PostSerializer(serializers.ModelSerializer):
  author = serializers.ReadOnlyField(source='author.username')
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    queryset = Post
    fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
    read_only_fields = ['author']
  
  