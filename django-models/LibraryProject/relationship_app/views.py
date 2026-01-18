from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.
def fbv_book_details(request):
  books = Book.objects.all()
  template = 'relationship_app/list_books.html'
  return render(request, template, {'books':books})

class CBV_library_details(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'