from django.urls import path
from .views import list_books, LibrayDetailView, LoginView, LogoutView, SignUpView
#LibraryDetailView

app_name='rel_app'
# views.register
urlpatterns = [
    path('fbv/', list_books, name='fbv_details'),
    path('cbv/<int:pk>/', LibrayDetailView.as_view(), name='cbv_details'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
]
