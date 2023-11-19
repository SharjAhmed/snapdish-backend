from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class CommentLikes(models.Model):
    """
    Class-based model for Comment Likes.
    """
    comment_liked = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment,
        related_name='comment_liked',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class Meta to set the order of the comments likes,
        newest first.
        """
        ordering = ['-created_at']
        unique_together = ['comment_liked', 'comment']

    def __str__(self):
        """
        Function to create the string for representing Comment Likes model
        in admin.
        """
        return f'{self.comment_liked} liked {self.comment}'