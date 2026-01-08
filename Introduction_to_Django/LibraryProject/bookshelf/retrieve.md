books = Book.objects.all()
for book in books:
  print(f"Title: {book.title}, Author: {book.author}, Year: {Book.publication_year}") 