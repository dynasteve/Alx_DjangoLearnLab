from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from .models import *

# Create your views here.
class BookListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
class BookDetailView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
class BookCreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
  
  def perform_create(self, serializer):
    serializer.save()

class BookUpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
  
  def perform_update(self, serializer):
    serializer.save()

class BookDeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
