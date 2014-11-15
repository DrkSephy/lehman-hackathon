from django.db import models

# Create your models here.

class AddClass(models.Model):
	class_name = models.CharField(maxlength=200)

	def __unicode__(self):
		return self.class_name

class StudentInfo(models.Model):
	number = models.IntegerField(default=0)
	email = models.CharField(maxlength=200)

	def __unicode__(self):
		return self.email, self.number