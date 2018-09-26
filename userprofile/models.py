from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=200)
	name = models.CharField(max_length=500)
	munny = models.IntegerField(default=0)
	def __str__(self):
		return self.username