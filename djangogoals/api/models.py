from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Goals(models.Model):
	"""Represents the goals model."""
	name = models.CharField(max_length=255, blank=False, unique=True)
	owner = models.ForeignKey('auth.User',
		related_name='goals',
		on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""String representation of model."""
		return "{}".format(self.name)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	"""Reciever handler creates tokens when a new user is created."""
	if created:
		Token.objects.create(user=instance)