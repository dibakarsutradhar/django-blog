from django.db import models

# Create your models here.
class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField(blank=True, default='')
	"""
	ForeignKey -> many-to-one relationship between current model and auth.user
	One user can be the author of many posts, but one post will have only one author
	related_name to set a custom access name for the posts model instead of default post_set
	It is added to the User serializer to complete the many-to-one relationship
	"""
	author = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.title

class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	body = models.TextField(blank=False)
	author = models.ForeignKey('auth.user', related_name='comments', on_delete=models.CASCADE)
	post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.body

class Category(models.Model):
	name = models.CharField(max_length=60, blank=False, default='')
	author = models.ForeignKey('auth.user', related_name='categories', on_delete=models.CASCADE)
	posts = models.ManyToManyField('Post', related_name='categories', blank=True)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
