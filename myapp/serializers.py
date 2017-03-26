from .models import Documents
from rest_framework import serializers

class DocumentSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Documents
		fields = ('Document','keyword')