from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.

class NewPost(models.Model):
	description = models.CharField(max_length=400)
	picture = models.ImageField(blank=False, upload_to='post_pictures')
	date = models.DateTimeField(default=datetime.now())
	user_info = models.ForeignKey('profile_app.ProfileInfo', on_delete=models.CASCADE, related_name='posts')
	liked_by = models.ManyToManyField('profile_app.ProfileInfo', related_name='likes', blank=True)

	def __str__(self):
		return "Post of {}".format(self.user_info.user.username)

class Comment(models.Model):
	text = models.CharField(max_length=400)
	date = models.DateTimeField(default=datetime.now())
	user_info = models.ForeignKey('profile_app.ProfileInfo', on_delete=models.CASCADE)
	post = models.ForeignKey(NewPost, on_delete=models.CASCADE, related_name='comment')

	def __str__(self):
		return "Comment of {}".format(self.user_info.user.username)