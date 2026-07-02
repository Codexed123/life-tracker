from rest_framework import serializers
from life_tracker_content.models import ActivitySerializer

class ActivityViewSet(serializers.ModelSerializer):
    class Meta:
        model = ActivitySerializer
        fields = '__all__'