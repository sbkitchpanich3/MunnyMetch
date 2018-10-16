from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, related_name = "profile", on_delete=models.CASCADE)
	munny = models.IntegerField(default=1000,null=True)
	wins = models.IntegerField(default=0,null=True)
	losses = models.IntegerField(default=0,null=True)
	matches = models.IntegerField(default=0,null=True)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
