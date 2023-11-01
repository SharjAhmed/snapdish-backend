from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializer.ReadOnlyField(source='owner.profile.id')
    profile_image = serializer.ReadOnlyField(
        source='owner.profile.image.url'
    )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'post',
            'created_at',
            'updated_at',
            'content'
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    post = serializer.ReadOnlyField(source='post.id')