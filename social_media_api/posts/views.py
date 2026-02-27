from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment, Like


# permissions.IsAuthenticated
# Post.objects.filter(author__in=following_users).order_by

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed_view(request):
    following_users = request.user.following.all()

    posts = Post.objects.filter(
        author__in=following_users
    ).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # serializer.save(author=self.request.user)
        
        comment = serializer.save(author=self.request.user)

        if comment.post.author != self.request.user:
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb="commented on your post",
                content_type=ContentType.objects.get_for_model(comment),
                object_id=comment.id
            )
        
class PostViewSet(viewsets.ModelViewSet):
    ...
    
    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()

        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post
        )

        if not created:
            return Response({"message": "Already liked."})

        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )

        return Response({"message": "Post liked."})

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()

        Like.objects.filter(
            user=request.user,
            post=post
        ).delete()

        return Response({"message": "Post unliked."})