from django.urls import path
from .views import list_books, LibrayDetailView

app_name='relationship_app'
urlpatterns = [
    path('fbv/', list_books, name='fbv_details'),
    path('cbv/<int:pk>', LibrayDetailView.as_view(), name='cbv_details'),
]
