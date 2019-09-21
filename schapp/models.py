from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):

	def __str__(self):
		res = str(self.username)
		return res

class Student(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length = 50,blank = False,null = False)
	age = models.IntegerField()
	is_adult = models.BooleanField(default = True)
	def __str__(self):
		return self.user.username;

