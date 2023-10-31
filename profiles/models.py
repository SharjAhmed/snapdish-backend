from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Class-based model for the profiles of users.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_avatar_kney3p'
    )

    class Meta:
        """
        Meta class to order profiles in order of most recently created.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Dunder string method to give information about who the profile owner is.
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a profile whenever a new user is created.
    Code taken from Code Institute's DRF API walkthrough project.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)