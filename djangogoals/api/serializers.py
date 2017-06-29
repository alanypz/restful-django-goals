from rest_framework import serializers
from .models import Goals


class GoalsSerializer(serializers.ModelSerializer):
	"""Maps model instances to JSON."""
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		"""Maps serializer fields to model fields."""
		model = Goals
		fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')
		