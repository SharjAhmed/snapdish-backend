from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Class-based model for user posts.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_iqkaz',
        blank=True
    )
    content = models.TextField(blank=True)

    class Meta:
        """
        Meta class to order psosts in order of most recently created.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Dunder string method to show post title and owner.
        """
        return f"'{self.title}' by {self.owner}"