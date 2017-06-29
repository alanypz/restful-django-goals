from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import GoalsSerializer
from .models import Goals
from .permissions import IsOwner


class CreateView(generics.ListCreateAPIView):
	"""Defines create behavior for restful api."""
	queryset = Goals.objects.all()
	serializer_class = GoalsSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner)

	def perform_create(self, serializer):
		"""Save post data when new goal model is created."""
		serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""Handles http get, put, and delete requests."""
	queryset = Goals.objects.all()
	serializer_class = GoalsSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner)