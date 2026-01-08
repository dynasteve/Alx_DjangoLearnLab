b1 = Book.objects.get(title="1984") 
b1.title = "Nineteen Eighty-Four"
b1.save()