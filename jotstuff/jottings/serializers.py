from rest_framework import serializers
from .models import Jotting

class JottingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Jotting
    fields = ('id', 'owner', 'title', 'body', 'created_at',)
