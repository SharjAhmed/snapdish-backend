from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Class-based model for likes, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        'unique_together' makes sure a user can't like the same post twice.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        """
        Dunder string method to give information about who has liked a post.
        """
        return f'{self.owner} liked {self.post}'