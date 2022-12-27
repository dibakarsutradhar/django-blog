from rest_framework import generics
from django.contrib.auth.models import User

from blog import serializers
from blog.models import Post

# Create your views here.
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer