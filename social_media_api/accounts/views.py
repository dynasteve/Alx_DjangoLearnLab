from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
# permissions.IsAuthenticated
# CustomUser.objects.all()

from .serializers import *

User = get_user_model()

class RegisterView(generics.CreateAPIView):
  queryset=User.objects.all()
  serializer_class=RegisterSerializer
  permission_classes=[AllowAny]
  
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(id=response.data['id'])
    token = Token.objects.get(user=user)
    
    return Response({
      "user": response.data,
      "token": token.key
    }, status=status.HTTP_201_CREATED)
    
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key
            })
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)

        if user_to_follow == request.user:
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)
        
        Notification.objects.create(
            recipient=user_to_follow,
            actor=request.user,
            verb="started following you",
            content_type=ContentType.objects.get_for_model(user_to_follow),
            object_id=user_to_follow.id
        )

        return Response({"message": "Successfully followed user."})

    except User.DoesNotExist:
        return Response(
            {"error": "User not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response({"message": "Successfully unfollowed user."})

    except User.DoesNotExist:
        return Response(
            {"error": "User not found."},
            status=status.HTTP_404_NOT_FOUND
        )