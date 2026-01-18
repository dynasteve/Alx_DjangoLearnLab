from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Library, Book

# Create your views here.
def list_books(request):
  books = Book.objects.all()
  template = 'relationship_app/list_books.html'
  return render(request, template, {'books':books})

class LibrayDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  
class UserLoginView(LoginView):
  template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
  template_name = 'relationship_app/logout.html'
  
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

