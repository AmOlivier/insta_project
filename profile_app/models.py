from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileinfo')
	bio = models.CharField(max_length=400)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
	facebook_link = models.URLField(blank=True)
	follows = models.ManyToManyField('ProfileInfo', symmetrical=False, blank=True)


	def __str__(self):
		return (self.user.username +' '+ str(self.id))
