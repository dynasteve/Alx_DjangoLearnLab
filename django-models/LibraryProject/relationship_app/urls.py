from django.urls import path
from .views import list_books, LibrayDetailView, UserLoginView, UserLogoutView, SignUpView
#LibraryDetailView

app_name='rel_app'
urlpatterns = [
    path('fbv/', list_books, name='fbv_details'),
    path('cbv/<int:pk>/', LibrayDetailView.as_view(), name='cbv_details'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
]
