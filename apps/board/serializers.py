from rest_framework import serializers

from .models import Board, Comment


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id') #'user.nickname'
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
    user = serializers.ReadOnlyField(source = 'user.id') #'user.nickname'
    class Meta:
        model = Comment
        fields = '__all__'
        # ['id', 'blog', 'user', 'created_at', 'comment']