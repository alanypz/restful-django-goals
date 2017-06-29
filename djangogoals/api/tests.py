from django.test import TestCase
from .models import Goals
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
	"""Test suite for Goals model."""

	def setUp(self):
		"""Set test client and other test variables."""
		user = User.objects.create(username="testableuser")
		self.goals_name = "Brush up on Django's Restful API."
		self.goals = Goals(name=self.goals_name,owner=user)

	def test_model_can_create_a_goal(self):
		"""Verify that model is successfully created."""
		old_count = Goals.objects.count()
		self.goals.save()
		new_count = Goals.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
	"""Test suite for api views."""

	def setUp(self):
		"""Set test client and other test variables."""
		user = User.objects.create(username="testableuser")
		self.client = APIClient()
		self.client.force_authenticate(user=user)

		self.goals_data = {'name': 'Run a 5k marathon.', 'owner': user.id}
		self.response = self.client.post(
			reverse('create'),
			self.goals_data,
			format='json')

	def test_api_can_create_goal(self):
		"""Verify that api can create a goal model."""
		self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
	
	def test_authorization_is_enforced(self):
		"""Verify that api has user authorization."""
		new_client = APIClient()
		response = new_client.get(
			'/goals/',
			kwargs={'pk': 3},
			format="json")
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_api_can_get_goal(self):
		"""Verify that api can get goal data."""
		goals = Goals.objects.get(id=1)
		response = self.client.get(
			'/goals/', 
			kwargs={'pk': goals.id},
			format='json')
		
		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, goals)

	def test_api_can_update_goal(self):
		"""Verify that api can update a specific goal model."""
		goals = Goals.objects.get()
		updated_goal = {'name': "An even more impress goal!"}
		response = self.client.put(
			reverse('details', kwargs={'pk': goals.id}),
			updated_goal,
			format='json'
		)
		self.assertEquals(response.status_code, status.HTTP_200_OK)

	def test_api_can_delete_goal(self):
		"""Verify that api can delete a goal model."""
		goals = Goals.objects.get()
		response = self.client.delete(
				reverse('details', kwargs={'pk': goals.id}),
				format='json',
				follow=True
			)
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)