from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = User
		fields = ['id', 'username', 'posts', 'comments']

class PostSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Post
		fields = ['id', 'title', 'body', 'author', 'comments']

class CommentSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Comment
		fields = ['id', 'body', 'author', 'post']