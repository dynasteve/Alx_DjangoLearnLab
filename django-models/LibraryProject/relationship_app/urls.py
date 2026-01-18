from django.urls import path
from . import views

app_name='relationship_app'
urlpatterns = [
    path('fbv/', views.fbv_book_details, name='fbv_details'),
    path('cbv/<int:pk>', views.CBV_library_details.as_view(), name='cbv_details'),
]
