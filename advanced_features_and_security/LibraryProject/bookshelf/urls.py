from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('add_book/', views.add_book, name='add_book'),
    path('list_books/', views.book_list, name='list_books'),
    path('read_book/<int:pk>', views.view_book, name='read_book'),
]
