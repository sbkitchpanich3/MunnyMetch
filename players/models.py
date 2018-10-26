from django.db import models
from django.conf import settings
from django.urls import reverse

class Stats(models.Model):
	player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	munny = models.IntegerField(default=1000)
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	matches = models.IntegerField(default=0)

class Challenge(models.Model):
	sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	munny = models.IntegerField(default=0)

