from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def fbv_book_details(request):
  books = Book.objects.all()
  template = 'relationship_app/list_books.html'
  return render(request, template, {'books':books})

class CBV_library_details(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'