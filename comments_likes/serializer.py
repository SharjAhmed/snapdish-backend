from django.db import IntegrityError
from rest_framework import serializers
from .models import CommentLikes


class CommentLikesSerializer(serializers.ModelSerializer):
    comment_liked = serializers.ReadOnlyField(
        source='comment_liked.username')

    class Meta:
        model = CommentLikes
        fields = [
            'id', 'comment_liked', 'created_at', 'comment',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })