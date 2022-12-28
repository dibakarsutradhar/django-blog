from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Comment, Category

class CommentSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Comment
		fields = ['body', 'author', 'post']

class CategorySerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Category
		fields = ['name', 'author', 'posts']

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.SerializerMethodField(required=False)
	# comments = serializers.SerializerMethodField(required=False)
	# comments = CommentSerializer()
	# total_comments = serializers.SerializerMethodField(required=False)
	categories = serializers.SerializerMethodField(required=False)

	class Meta:
		model = User
		fields = ['username', 'posts', 'categories']

	def get_posts(self, user):
		post_list = []
		user_posts = Post.objects.filter(author = user)
		for post in user_posts:
			post_list.append({
				'title': post.title,
				'body': post.body,
				'created': post.created
			})
		return post_list

	def get_categories(self, user):
		category_list = []
		user_categories = Category.objects.filter(author = user)
		for category in user_categories:
			category_list.append({
				'name': category.name
			})
		return category_list

	# def get_total_comments(self, user):
	# 	comment_list = []
	# 	total_comments = Comment.objects.filter(author = user)
	# 	for comment in total_comments:
	# 		comment_list.append({
	# 			'total_comment': comment.pk
	# 		})
	# 	return total_comments

	"""
	comments.object.filter(author = user.count())
	"""

class PostSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	comments = serializers.SerializerMethodField(required=False)
	categories = serializers.SerializerMethodField(required=False)

	class Meta:
		model = Post
		fields = '__all__'

	def get_comments(self, post):
		comment_list = []
		user_comments = Comment.objects.filter(post = post)
		for comment in user_comments:
			comment_list.append({
				'body': comment.body,
				'author': comment.author.username,
				'created': comment.created
			})
		return comment_list

	def get_categories(self, post):
		category_list = []
		user_categories = Category.objects.filter(posts = post)
		for category in user_categories:
			category_list.append({
				'name': category.name
			})
		return category_list