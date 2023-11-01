from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Class-based model for followers
    """
    owner = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        """
        Dunder string method to give information about a users following.
        """
        return f'{self.owner} follows {self.followed}'