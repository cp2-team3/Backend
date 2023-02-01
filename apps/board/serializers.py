from rest_framework import serializers

from .models import Board, Comment


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname') #'user.nickname'
    hit = serializers.IntegerField(read_only=True)

    class Meta:
        model = Board
        fields = '__all__'
        # fields = (
        #     'id',
        #     'user',
        #     'title',
        #     'content',
        #     'created_at',
        #     'updated_at',
        #     'hit',
        #     'catagory',
        #     'uploadimages',
        #     'uploadfiles'
        # )
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname') #'user.nickname'
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'created_at', 'comment']