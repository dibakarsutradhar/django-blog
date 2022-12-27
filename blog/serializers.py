from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Comment, Category

class CommentSerializer(serializers.ModelSerializer):
	# author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Comment
		fields = ['id', 'body', 'author', 'post']

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	# comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	comments = CommentSerializer(required=False, read_only=True)
	categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = User
		fields = ['id', 'username', 'posts', 'comments', 'categories']

class PostSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Post
		fields = ['id', 'title', 'body', 'author', 'comments', 'categories']

class CategorySerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Category
		fields = ['id', 'name', 'author', 'posts']