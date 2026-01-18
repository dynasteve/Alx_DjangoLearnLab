from .models import *

author_name = "a"
author_obj = Author.objects.get(name=author_name)
author_obj.books.all()

# author_obj.objects.filter(author=author)

library_name = "library"
library_obj = Library.objects.get(name=library_name)
library_obj.books.all()

library_name = "library"
librarian = library_obj.librarian