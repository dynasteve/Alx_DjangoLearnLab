from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']
    
  def create(self, validated_data):
    password = validated_data.pop('password')
    del validated_data['password2']
    user = User.objects.create(**validated_data)
    user.set_password(password)
    user.save()
    # get_user_model().objects.create_user
    
    Token.objects.create(user=user)
    return user
  
class UserSerializer(serializers.ModelSerializer):
  followers_count = serializers.SerializerMethodField()
  following_count = serializers.SerializerMethodField()
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'bio', 'profile_picture']
    
  def get_followers_count(self, obj):
        return obj.followers.count()

  def get_following_count(self, obj):
      return obj.following.count()