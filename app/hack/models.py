from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class StudentInfo(models.Model):
	number = models.IntegerField(default=0)
	email = models.CharField(max_length=200)

	def __unicode__(self):
		return self.email



class AddClass(models.Model):
	class_name = models.CharField(max_length=200)
	students = models.ManyToManyField(StudentInfo, null=True)



	def __unicode__(self):
		return self.class_name



class Notification(models.Model):
	class_name = models.CharField(max_length=50)
	timeStamp = models.CharField(max_length=50)
	note = models.CharField(max_length=300)
