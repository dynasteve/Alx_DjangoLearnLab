from .models import *

author = "a"
author_obj = Author.objects.get(name = author)
author_obj.books.objects.all()

library_name = "library"
library_obj = Library.objects.get(name=library_name)
library_obj.books.all()

librarian = "librarian"
librarian_obj = Librarian.objects.get(name = librarian)
librarian_obj.library.all()