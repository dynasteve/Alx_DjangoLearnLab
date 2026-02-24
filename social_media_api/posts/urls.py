from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed_view
from django.urls import path

# permissions.IsAuthenticated
# Post.objects.filter(author__in=following_users).order_by

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('feed/', feed_view, name='feed'),
]