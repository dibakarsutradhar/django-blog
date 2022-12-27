from rest_framework import generics
from blog import serializers
from django.contrib.auth.models import User

# Create your views here.
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer