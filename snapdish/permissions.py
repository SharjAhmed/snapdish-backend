from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user

class CommenterOrReadOnly(permissions.BasePermission):
    """
    Custom permission created to allow commenters to edit their comments only.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.commenter == request.user

class CommentLikedOrReadOnly(permissions.BasePermission):
    """
    Custom permission created to allow only the user who has liked a comment to delete their
    like from comments.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.comment_liked == request.user