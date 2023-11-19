from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from snapdish.permissions import CommentLikedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import CommentLikes
from .serializer import CommentLikesSerializer


class ListCommentLikes(generics.ListCreateAPIView):
    """
    Class-based view to list all comment likes.
    """
    queryset = CommentLikes.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikesSerializer

    def perform_create(self, serializer):
        comment = get_object_or_404(
            Comment, pk=serializer.initial_data['comment'])
        if comment.commenter == self.request.user:
            raise PermissionDenied
        else:
            serializer.save(comment_liked=self.request.user)


class DetailCommentLikes(generics.RetrieveDestroyAPIView):
    queryset = CommentLikes.objects.all()
    permission_classes = [CommentLikedOrReadOnly]
    serializer_class = CommentLikesSerializer