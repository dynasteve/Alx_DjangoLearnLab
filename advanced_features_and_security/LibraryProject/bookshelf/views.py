from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Book
from .forms import CreateBookForm

def index(request):
  return render(request, 'bookshelf/index.html')

@permission_required('can_add_book', raise_exception=True)
def add_book(request):
  if request.method == "POST":
    form = CreateBookForm(request.POST)
    if form.is_valid():
      new_book = form.save()
      messages.success(request, f"\"{new_book.title}\" was successfully added to Library")
      return redirect('/')
  else:
    form = CreateBookForm()
    
  context = {'form': form}
  return render(request, 'crud_book/add_book.html', context)