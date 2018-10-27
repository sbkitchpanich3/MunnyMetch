from django.db import models
from django.conf import settings
from django.urls import reverse

class Challenge(models.Model):
	sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="sender")
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="receiver")
	bet = models.IntegerField(default=0)
	status = models.IntegerField(default=0)
	p1result = models.BooleanField(null=True)
	p2result = models.BooleanField(null=True)