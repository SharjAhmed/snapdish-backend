from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile


class Comment(models.Model):
    """
    Class-based model for comments.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
