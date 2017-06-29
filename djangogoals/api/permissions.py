from rest_framework.permissions import BasePermission
from .models import Goals


class IsOwner(BasePermission):
	"""Custom permissions. Permits ownly model owners to edit models."""

	def has_object_permission(self, request, view, obj):
		if isinstance(obj, Goals):
			return obj.owner == request.user
		return obj.owner == request.user