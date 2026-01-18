from django.urls import path
from .views import list_books, LibrayDetailView, 
from . import views
#LibraryDetailView

app_name='rel_app'
urlpatterns = [
    path('fbv/', list_books, name='fbv_details'),
    path('cbv/<int:pk>/', LibrayDetailView.as_view(), name='cbv_details'),
    path('login/', views.UserLoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),
    path('logout/', views.UserLogoutView.as_view(template_name = 'relationship_app/logout.html'), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
]
