from __future__ import unicode_literals

from django.db import models

# Create your models here.

class formfill(models.Model):
	full_name = models.CharField(max_length=80)
	email = models.EmailField()
	college_name = models.CharField(max_length=100)
	college_place = models.CharField(max_length=50)
	phone_no = models.IntegerField()
	skill1 = models.CharField(max_length=25)
	branch = models.CharField(max_length=30)
	year = models.DateField()
	post = models.TextField()
	profile_image = models.FileField(blank= True, null=True)
	#login_name = models.ForeignKey(User, on_delete=models.CASCADE)
	

	def __unicode__(self):
		return self.email

	def __unicode__(self):
		return self.full_name
