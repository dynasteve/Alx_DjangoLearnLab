from django.urls import path
import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='list_books'),
    path('books/create', views.BookCreateView.as_view(), name='create_books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>', views.BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),
]
