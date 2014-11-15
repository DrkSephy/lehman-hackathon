from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AddClass(models.Model):
	class_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.class_name

class StudentInfo(models.Model):
	number = models.IntegerField(default=0)
	email = models.CharField(max_length=200)

	def __unicode__(self):
		return self.email
